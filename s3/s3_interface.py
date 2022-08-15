import boto3
from . import settings

s3 = boto3.resource(
    's3',
    aws_access_key_id=settings.KEY_ID,
    aws_secret_access_key=settings.SECRET_KEY,
    region_name=settings.REGION
)

# return all images in IDVA S3 bucket
def list_files(bucket_name):
    bucket = s3.Bucket(bucket_name)
    contents = []
    for item in bucket.objects.filter(Prefix="storage/company/"):
        contents.append(item)

    return contents

# return specific file from bucket to be stored in temp local file
def get_file(key, bucket_name, tmp):
    bucket = s3.Bucket(bucket_name)
    
    with open(tmp.name, 'wb') as f:
        bucket.download_fileobj(key, f)
        src = tmp.name

    return src
    