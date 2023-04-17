import pytest
import base64
import tempfile

from s3 import s3_interface


def test_get_image_pass(s3_client, s3_test, bucket_name):
    tmp = tempfile.NamedTemporaryFile()

    res = s3_interface.get_file(s3_client, bucket_name, "penguin.jpg", tmp)

    with open("./s3/tests/images/penguin.jpg", "rb") as img:
        b64_og = base64.b64encode(img.read()).decode("utf-8")

    with open(res, "rb") as img:
        b64_new = base64.b64encode(img.read()).decode("utf-8")

    assert b64_og == b64_new


def test_get_image_not_found(s3_client, s3_test, bucket_name):
    tmp = tempfile.NamedTemporaryFile()
    try:
        s3_interface.get_file(s3_client, bucket_name, "does_not_exist", tmp)
        assert False
    except FileNotFoundError:
        assert True
