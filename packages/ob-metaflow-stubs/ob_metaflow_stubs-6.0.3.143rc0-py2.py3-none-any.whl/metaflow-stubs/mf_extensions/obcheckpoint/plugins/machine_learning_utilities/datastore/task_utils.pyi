######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.14.0.2rc0+obcheckpoint(0.1.8.1rc0);ob(v1)                                            #
# Generated on 2025-02-17T19:27:36.073978                                                            #
######################################################################################################

from __future__ import annotations

import typing
import metaflow
if typing.TYPE_CHECKING:
    import metaflow.exception
    import metaflow

from ......metaflow_current import current as current
from ......exception import MetaflowException as MetaflowException
from .context import datastore_context as datastore_context

TYPE_CHECKING: bool

class UnresolvableDatastoreException(metaflow.exception.MetaflowException, metaclass=type):
    ...

def init_datastorage_object():
    ...

def resolve_storage_backend(pathspec: typing.Union[str, "metaflow.Task"] = None):
    ...

class FlowNotRunningException(metaflow.exception.MetaflowException, metaclass=type):
    ...

def storage_backend_from_flow(flow: "metaflow.FlowSpec"):
    ...

