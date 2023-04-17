import pytest
import base64
import tempfile

from s3 import s3_interface


def test_delete_image_pass(s3_client, s3_test, bucket_name):
    tmp = tempfile.NamedTemporaryFile()

    res = s3_interface.get_file(s3_client, bucket_name, "penguin.jpg", tmp)

    with open(res, "rb") as img:
        b64_new = base64.b64encode(img.read()).decode("utf-8")

    assert b64_new

    s3_interface.delete_file(s3_client, bucket_name, "penguin.jpg")
    try:
        res = s3_interface.get_file(s3_client, bucket_name, "penguin.jpg", tmp)
        assert False
    except FileNotFoundError:
        assert True
