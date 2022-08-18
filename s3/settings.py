"""
Configuration for the S3 Interface microservice settings.
"""
import json
import logging
import os

log = logging.getLogger(__name__)

def get_s3_info():
    vcap_services = os.getenv("VCAP_SERVICES", "")
    try:
        key_id = json.loads(vcap_services)["s3"][0]["credentials"]["access_key_id"]
        secret_key = json.loads(vcap_services)["s3"][0]["credentials"]["secret_access_key"]
        region = json.loads(vcap_services)["s3"][0]["credentials"]["region"]
        bucket = json.loads(vcap_services)["s3"][0]["credentials"]["bucket"]
    except (json.JSONDecodeError, KeyError) as err:
        log.warning("Unable to load info from VCAP_SERVICES")
        log.debug("Error: %s", str(err))
        key_id = ""
        secret_key = ""
        region = ""
        bucket = ""
    
    return (key_id, secret_key, region, bucket)

PORT = 8080

KEY_ID, SECRET_KEY, REGION, BUCKET = get_s3_info()