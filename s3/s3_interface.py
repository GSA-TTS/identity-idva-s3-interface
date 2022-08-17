import boto3
import base64
import tempfile
from . import settings

s3 = boto3.resource(
    's3',
    aws_access_key_id=settings.KEY_ID,
    aws_secret_access_key=settings.SECRET_KEY,
    region_name=settings.REGION
)
bucket = s3.Bucket(settings.BUCKET)


def list_files():
    """
    return all images in IDVA S3 bucket
    """
    contents = []
    for item in bucket.objects.filter(Prefix="storage/company/"):
        contents.append(item)

    return contents


def get_file(key):
    """
    return specific file in base64 format from bucket to be stored in temp local file
    """
    tmp = tempfile.NamedTemporaryFile()

    # save file
    with open(tmp.name, 'wb') as f:
        bucket.download_fileobj(key, f)

    # read and convert file to base64
    with open(tmp.name, 'rb') as f:
        b64 = base64.b64encode(f.read())

    return b64.decode('utf-8')


def delete_file(key):
    return bucket.delete_objects(Delete={
        "Objects": [
            {"Key": key}
        ]
    })
