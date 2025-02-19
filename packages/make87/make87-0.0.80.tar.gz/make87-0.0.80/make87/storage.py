import os
from pathlib import Path

from make87 import APPLICATION_ID, DEPLOYED_APPLICATION_ID, DEPLOYED_SYSTEM_ID


def get_system_storage_path() -> Path:
    """Returns the path to the system storage directory."""
    path = Path("/tmp/make87") / DEPLOYED_SYSTEM_ID
    if "MAKE87_STORAGE_PATH" in os.environ:
        storage_url = os.environ["MAKE87_STORAGE_PATH"]
        endpoint_url = os.environ["MAKE87_STORAGE_ENDPOINT_URL"]
        access_key = os.environ.get("MAKE87_STORAGE_ACCESS_KEY")
        secret_key = os.environ.get("MAKE87_STORAGE_SECRET_KEY")

        try:
            from s3path import S3Path
            from s3path.old_versions import _S3Accessor

            S3Path._accessor = _S3Accessor(
                endpoint_url=endpoint_url,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key
            )

            path = S3Path(storage_url)

        except ImportError:
            raise ImportError(
                "Please install make87[storage] to use the cloud storage functionality."
            )

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_organization_storage_path() -> Path:
    """Returns the path to the organization storage directory."""
    path = get_system_storage_path().parent
    return path

def get_application_storage_path() -> Path:
    """Returns the path to the application storage directory."""
    path = get_system_storage_path() / APPLICATION_ID
    return path

def get_deployed_application_storage_path() -> Path:
    """Returns the path to the deployed application storage directory."""
    path = get_system_storage_path() / DEPLOYED_APPLICATION_ID
    return path