import boto3
import pytest

from moto import mock_s3


@pytest.fixture
def s3_client():
    with mock_s3():
        s3 = boto3.client(
            "s3",
            aws_access_key_id="testing",
            aws_secret_access_key="testing",
            region_name="us-east-1",
        )
        yield s3


@pytest.fixture
def bucket_name():
    return "my-test-bucket"


@pytest.fixture
def s3_test(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    s3_client.upload_file(
        Filename="./s3/tests/images/penguin.jpg", Bucket=bucket_name, Key="penguin.jpg"
    )
