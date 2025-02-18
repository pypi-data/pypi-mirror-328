######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.14.0.2rc0+obcheckpoint(0.1.8.1rc0);ob(v1)                                            #
# Generated on 2025-02-17T19:27:36.051021                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception
    import metaflow.mf_extensions.obcheckpoint.plugins.machine_learning_utilities.datastore.context
    import metaflow

from ......exception import MetaflowException as MetaflowException

TYPE_CHECKING: bool

ARTIFACT_STORE_CONFIG_ENV_VAR: str

class UnresolvableDatastoreException(metaflow.exception.MetaflowException, metaclass=type):
    ...

class ArtifactStoreContext(object, metaclass=type):
    """
    This class will act as a singleton to switch the datastore so that
    Any checkpoint operations will be done in the correct datastore. This
    can be a useful way of short-circuting a datastore switch between runtime
    And post-runtime retrieval operations.
    """
    @property
    def MF_DATASTORES(self):
        ...
    def __init__(self):
        ...
    def flow_init_context(self, context):
        ...
    def post_task_runtime_context(self, context):
        ...
    def switch_context(self, context):
        ...
    def get(self):
        ...
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
        ...
    def to_task_metadata(self):
        ...
    def default(self):
        ...
    ...

datastore_context: ArtifactStoreContext

def using_artifact_store(type, config):
    """
    This context manager can be used to switch the artifact store
    for a block of code. This is useful when users maybe accessing
    checkpoints/models from a different datastore using the
    `@with_artifact_store` decorator.
    """
    ...

