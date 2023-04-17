import boto3


def get_clients(s3_credentials):
    """
    creates list of boto3 s3 clients from list of s3 credentials
    """
    s3_clients = {}
    for credentials in s3_credentials:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=s3_credentials[credentials]["key_id"],
            aws_secret_access_key=s3_credentials[credentials]["secret_key"],
            region_name=s3_credentials[credentials]["region"],
        )
        s3_clients[credentials] = s3_client
    return s3_clients


def get_file(s3_client, bucket, key, tmp):
    """
    return specific file in base64 format from bucket to be stored in temp local file
    """

    # save file
    try:
        with open(tmp.name, "wb") as f:
            s3_client.download_fileobj(bucket, key, f)
    except:
        raise FileNotFoundError

    return tmp.name


def delete_file(s3_client, bucket, key):
    """
    deletes specific file
    """
    return s3_client.delete_object(Bucket=bucket, Key=key)
