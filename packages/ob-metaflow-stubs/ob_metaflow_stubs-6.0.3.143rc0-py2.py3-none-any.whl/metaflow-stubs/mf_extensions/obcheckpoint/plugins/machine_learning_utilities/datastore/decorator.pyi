######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.14.0.2rc0+obcheckpoint(0.1.8.1rc0);ob(v1)                                            #
# Generated on 2025-02-17T19:27:36.102835                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.decorators

from ......metadata_provider.metadata import MetaDatum as MetaDatum
from ......exception import MetaflowException as MetaflowException

class ArtifactStoreFlowDecorator(metaflow.decorators.FlowDecorator, metaclass=type):
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
    def flow_init(self, flow, graph, environment, flow_datastore, metadata, logger, echo, options):
        ...
    ...

def set_datastore_context(flow, metadata, run_id, step_name, task_id, retry_count):
    ...

