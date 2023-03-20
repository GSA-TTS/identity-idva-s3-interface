import boto3
import pytest

from moto import mock_s3


@pytest.fixture
def s3_resource():
    with mock_s3():
        s3 = boto3.client(
            "s3",
            aws_access_key_id="testing",
            aws_secret_access_key="testing",
            region_name="us-east-1",
        )
        yield s3
