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
        credentials = json.loads(vcap_services)["s3"][0]["credentials"]
    except (json.JSONDecodeError, KeyError) as err:
        log.warning("Unable to load info from VCAP_SERVICES")
        log.debug("Error: %s", str(err))
        raise Exception(str(err))

    key_id = credentials["access_key_id"]
    secret_key = credentials["secret_access_key"]
    region = credentials["region"]
    bucket = credentials["bucket"]
    return (key_id, secret_key, region, bucket)


PORT = int(os.getenv("PORT", 8080))
HOST = '0.0.0.0'

KEY_ID, SECRET_KEY, REGION, BUCKET = get_s3_info()
