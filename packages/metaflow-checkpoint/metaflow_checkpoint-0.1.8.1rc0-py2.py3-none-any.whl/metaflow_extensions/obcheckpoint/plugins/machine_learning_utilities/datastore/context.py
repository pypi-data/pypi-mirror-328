from typing import Union, Optional, TYPE_CHECKING
from metaflow.exception import MetaflowException
import sys

# import context manager
from contextlib import contextmanager
import os
import json

ARTIFACT_STORE_CONFIG_ENV_VAR = "METAFLOW_CHECKPOINT_ARTIFACT_STORE_CONFIG"

if TYPE_CHECKING:
    import metaflow


class UnresolvableDatastoreException(MetaflowException):
    pass


class ArtifactStoreContext:

    """
    This class will act as a singleton to switch the datastore so that
    Any checkpoint operations will be done in the correct datastore. This
    can be a useful way of short-circuting a datastore switch between runtime
    And post-runtime retrieval operations.
    """

    current_context = None  # dict

    _MF_DATASTORES = None

    @property
    def MF_DATASTORES(self):
        if self._MF_DATASTORES is None:
            from metaflow.plugins import DATASTORES

            self._MF_DATASTORES = DATASTORES
        return self._MF_DATASTORES

    def __init__(self):
        if ARTIFACT_STORE_CONFIG_ENV_VAR in os.environ:
            self.switch_context(json.loads(os.environ[ARTIFACT_STORE_CONFIG_ENV_VAR]))

    def flow_init_context(self, context):
        if context is None:
            self.switch_context(None)
        required_context_keys = ["type", "config"]
        required_config_keys = [
            "root",
        ]
        if not all([k in context for k in required_context_keys]):
            raise ValueError("Context does not have all required keys.")
        if not all([k in context["config"] for k in required_config_keys]):
            raise ValueError("Config does not have all required keys.")
        os.environ[ARTIFACT_STORE_CONFIG_ENV_VAR] = json.dumps(context)
        self.switch_context(context)

    def post_task_runtime_context(self, context):
        required_context_keys = ["type", "config"]
        if not all([k in context for k in required_context_keys]):
            raise ValueError("Context does not have all required keys.")
        # In these situations, if the root is not specified it might be
        # okay, since we can have a default root for the datastore
        self.switch_context(context)

    def switch_context(self, context):
        self.current_context = context

    def get(self):
        if self.current_context is None:
            return self.default()
        return self._from_current_context()

    def _from_current_context(self):
        # from metaflow.plugins import DATASTORES
        _type = self._runtime_ds_type(self.current_context["type"])
        _config = self.current_context["config"].copy()
        root = _config.pop("root")
        storage_impl = [d for d in self.MF_DATASTORES if d.TYPE == _type][0]
        return storage_impl(root, **_config)

    def _runtime_ds_type(self, ds_type):
        # Hack ; Ideally all datastores should have better
        # abstractions upstream. This will help handle the
        # case where we don't need to vendor the `s3-compatible`
        # datastore in the plugin
        if ds_type == "s3":
            return "s3-compatible"
        return ds_type

    def _task_metadata_ds_type(self, ds_type):
        # Hack ; Ideally all datastores should have better
        # abstractions upstream. This will help handle the
        # case where we don't need to vendor the `s3-compatible`
        # datastore in the plugin
        if ds_type == "s3-compatible":
            return "s3"
        return ds_type

    def from_task_metadata(self, task: "metaflow.Task"):
        """
        TODO: This is not the best way to do this since this is mostly used for
        listing checkpoints post-runtime. It is also currently a code path for
        `Checkpoint.list()` but it can be clunky and I havent thought throught its
        implications on other code paths. Currently it can work with :
        ```
        config = {
            "client_params":{
                "access_key_id": "abc",
                "secret_access_key": "xyz"
            }
        }
        with using_artifact_store(type="s3", config=config):
            Checkpoint().load(Checkpoint().list(task=task)[0], "my-path")
        ```
        """
        metadata = task.metadata_dict
        md_keys = ["artifact-store-ds-type", "artifact-store-ds-root"]
        if all([k in metadata for k in md_keys]):
            _fresh_context = ArtifactStoreContext()
            _config = {}
            if (
                self.current_context is not None
                and self.current_context["type"] == metadata["artifact-store-ds-type"]
            ):
                _config = self.current_context["config"].copy()
                _config.pop("root", None)
            _switched_context = {
                "type": metadata["artifact-store-ds-type"],
                "config": {
                    # only set the root from here.
                    # The other config options can come from
                    # the current context's defaults
                    "root": metadata["artifact-store-ds-root"],
                    **_config,
                },
            }
            # print("Switching context from metadata", _switched_context, file=sys.stderr)

            _fresh_context.switch_context(_switched_context)
            return _fresh_context.get()

        # print(
        #     "Could not find artifact store metadata in task metadata. Using default context.",
        #     file=sys.stderr,
        # )
        ds_type = metadata.get("ds-type", None)
        if ds_type is None:
            raise UnresolvableDatastoreException(
                "Could not find datastore type in metadata for task %s" % task.pathspec
            )
        ds_root = metadata.get("ds-root", None)
        _type = self._runtime_ds_type(ds_type)
        storage_impl = [d for d in self.MF_DATASTORES if d.TYPE == _type][0]
        if ds_root is None:
            ds_root = storage_impl.get_datastore_root_from_config(print)

        return storage_impl(ds_root)

    def to_task_metadata(self):
        _ds = self.get()
        return {
            "artifact-store-ds-type": self._task_metadata_ds_type(_ds.TYPE),
            "artifact-store-ds-root": _ds.datastore_root,
        }

    def default(self):
        from metaflow.metaflow_config import DEFAULT_DATASTORE

        search_datastore = self._runtime_ds_type(DEFAULT_DATASTORE)

        storage_impl = [d for d in self.MF_DATASTORES if d.TYPE == search_datastore][0]
        return storage_impl(storage_impl.get_datastore_root_from_config(print))


datastore_context = ArtifactStoreContext()


@contextmanager
def using_artifact_store(type, config):
    """
    This context manager can be used to switch the artifact store
    for a block of code. This is useful when users maybe accessing
    checkpoints/models from a different datastore using the
    `@with_artifact_store` decorator.
    """
    _context = {
        "type": type,
        "config": config,
    }
    try:
        datastore_context.post_task_runtime_context(_context)
        yield
    finally:
        datastore_context.switch_context(None)
