"""Utils file."""

import os

import dinamis_sdk
import dinamis_sdk.settings


def set_secret_key_env():
    """Test diff."""
    if "DINAMIS_SDK_ACCESS_KEY" in os.environ:
        dinamis_sdk.settings.ENV.dinamis_sdk_access_key = os.environ.get(
            "DINAMIS_SDK_ACCESS_KEY"
        )
    if "DINAMIS_SDK_SECRET_KEY" in os.environ:
        dinamis_sdk.settings.ENV.dinamis_sdk_secret_key = os.environ.get(
            "DINAMIS_SDK_SECRET_KEY"
        )
