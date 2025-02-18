# THIS FILE IS ALSO USED (Figure where is the best place to put it.)
from typing import Union, Optional, TYPE_CHECKING
from metaflow import current
from metaflow.exception import MetaflowException
from .context import datastore_context

if TYPE_CHECKING:
    import metaflow


class UnresolvableDatastoreException(MetaflowException):
    pass


def init_datastorage_object():
    return datastore_context.get()


def resolve_storage_backend(pathspec: Union[str, "metaflow.Task"] = None):
    from metaflow.client.core import Task

    if isinstance(pathspec, Task):
        return datastore_context.from_task_metadata(pathspec)
    elif isinstance(pathspec, str):
        if len(pathspec.split("/")) != 4:
            raise ValueError("Pathspec is not of the correct format.")
        return datastore_context.from_task_metadata(Task(pathspec))
    else:
        raise ValueError(
            "Pathspec is of invalid type. It should be either a string or a Task object but got %s"
            % type(pathspec)
        )


class FlowNotRunningException(MetaflowException):
    pass


def storage_backend_from_flow(flow: "metaflow.FlowSpec"):
    if not current.is_running_flow:
        raise FlowNotRunningException
    return datastore_context.get()
