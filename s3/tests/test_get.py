import pytest
import base64
import tempfile

from s3 import s3_interface


@pytest.fixture
def bucket_name():
    return "my-test-bucket"


@pytest.fixture
def s3_test(s3_resource, bucket_name):
    s3_resource.create_bucket(Bucket=bucket_name)
    s3_resource.Bucket(bucket_name).upload_file(
        "./s3/tests/images/penguin.jpeg", "penguin.jpeg"
    )


def test_get_image_pass(s3_resource, s3_test, bucket_name):
    tmp = tempfile.NamedTemporaryFile()

    res = s3_interface.get_file("penguin.jpeg", s3_resource.Bucket(bucket_name), tmp)

    with open(res, "rb") as img:
        b64_new = base64.b64encode(img.read()).decode("utf-8")

    assert b64_new


def test_get_image_not_found(s3_resource, s3_test, bucket_name):
    tmp = tempfile.NamedTemporaryFile()
    try:
        s3_interface.get_file("does_not_exist", s3_resource.Bucket(bucket_name), tmp)
    except FileNotFoundError:
        assert True
    else:
        assert False
