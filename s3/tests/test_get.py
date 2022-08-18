import pytest
import base64

from s3.s3_interface import S3Interface
from tempfile import NamedTemporaryFile


@pytest.fixture
def bucket_name():
    return "my-test-bucket"


@pytest.fixture
def s3_test(s3_resource, bucket_name):
    s3_resource.create_bucket(Bucket=bucket_name)
    s3_resource.Bucket(bucket_name).upload_file('./s3/tests/images/penguin.jpg', 'penguin.jpg')

def test_get_image_pass(s3_resource, s3_test, bucket_name):
    with open('./s3/tests/images/penguin.jpg', 'rb') as img:
        b64 = base64.b64encode(img.read()).decode('utf-8')
    
    res = S3Interface.get_file('penguin.jpg', s3_resource.Bucket(bucket_name))

    assert res == b64

def test_get_image_not_found(s3_resource, s3_test, bucket_name):
    try:
        S3Interface.get_file('does_not_exist', s3_resource.Bucket(bucket_name))
    except FileNotFoundError:
        assert True
    else:
        assert False