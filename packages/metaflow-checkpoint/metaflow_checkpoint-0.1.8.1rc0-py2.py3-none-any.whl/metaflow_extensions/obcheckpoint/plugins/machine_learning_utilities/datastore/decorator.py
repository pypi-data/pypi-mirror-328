from metaflow.decorators import FlowDecorator, StepDecorator
from metaflow.metadata_provider import MetaDatum
from metaflow.exception import MetaflowException


class ArtifactStoreFlowDecorator(FlowDecorator):
    """
    Allows setting external datastores to save data for the
    `@checkpoint`/`@model`/`@huggingface_hub` decorators. This is useful
    when the compute medium lives in a different geographical location
    than metaflow's datastore (e.g. S3, GCS, Azure Blob Storage).

    Parameters:
    ----------

    type: str
        The type of the datastore. Can be one of 's3', 'gcs', 'azure' or any other supported metaflow Datastore.

    config: dict or Callable
        Dictionary of configuration options for the datastore. The following keys are required:
        - root: The root path in the datastore where the data will be saved. (needs to be in the format expected by the datastore)
            - example: 's3://bucket-name/path/to/root'
            - example: 'gs://bucket-name/path/to/root'
            - example: 'https://myblockacc.blob.core.windows.net/metaflow/'
        - role_arn (optional): AWS IAM role to access s3 bucket (only when `type` is 's3')
        - session_vars (optional): AWS session variables to access s3 bucket (only when `type` is 's3')
        - client_params (optional): AWS client parameters to access s3 bucket (only when `type` is 's3')

    """

    name = "with_artifact_store"
    defaults = {
        "type": None,  # can be one of 's3', 'gcs', 'azure'
        "config": None,  # Dictionary of configuration options
    }

    def flow_init(
        self, flow, graph, environment, flow_datastore, metadata, logger, echo, options
    ):
        cannot_be_none = ["type", "config"]
        for k in cannot_be_none:
            if self.attributes[k] is None:
                raise MetaflowException(
                    f"@{self.name} cannot have {k} be set to `None`."
                )


def set_datastore_context(flow, metadata, run_id, step_name, task_id, retry_count):
    from .context import datastore_context

    _flw_deco = None
    for decorators in flow._flow_decorators.values():
        for dec in decorators:
            if isinstance(dec, ArtifactStoreFlowDecorator):
                _flw_deco = dec
        else:
            continue

    if _flw_deco is None:
        # print("No datastore context found to set")
        return None

    _config = _flw_deco.attributes["config"]
    # Check if the config is a callable lambda
    if callable(_flw_deco.attributes["config"]):
        _config = _flw_deco.attributes["config"]()

    datastore_context.flow_init_context(
        {"type": _flw_deco.attributes["type"], "config": _config}
    )

    task_md = datastore_context.to_task_metadata()
    entries = [
        MetaDatum(
            field=k,
            value=v,
            type="mf-checkpoint-artifact-store",
            tags=[
                "attempt_id:%s" % str(retry_count),
            ],
        )
        for k, v in task_md.items()
    ]
    metadata.register_metadata(run_id, step_name, task_id, entries)
