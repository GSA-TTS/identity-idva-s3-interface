"""
Configuration for the S3 Interface microservice settings.
"""
import json
import logging
import os

log = logging.getLogger(__name__)


def get_s3_info():
    vcap_services = os.getenv("VCAP_SERVICES")
    try:
        service_list = json.loads(vcap_services)["s3"]
    except (json.JSONDecodeError, KeyError) as err:
        log.warning("Unable to load info from VCAP_SERVICES")
        log.debug("Error: %s", str(err))
        raise Exception(str(err))

    s3_credentials = {}

    for service in service_list:
        credentials = service["credentials"]
        s3_credentials[service["name"]] = {
            "key_id": credentials["access_key_id"],
            "secret_key": credentials["secret_access_key"],
            "region": credentials["region"],
            "bucket": credentials["bucket"],
        }

    return s3_credentials


PORT = int(os.getenv("PORT", 8080))
HOST = "0.0.0.0"  # nosec

S3_CREDENTIALS = get_s3_info()
