import boto3
import tempfile
import mimetypes
from flask import Flask, jsonify, request, send_file
from s3 import s3_interface
from s3 import settings

s3 = boto3.resource(
    "s3",
    aws_access_key_id=settings.KEY_ID,
    aws_secret_access_key=settings.SECRET_KEY,
    region_name=settings.REGION,
)
bucket = s3.Bucket(settings.BUCKET)

app = Flask(__name__)


@app.route("/get", methods=["GET"])
def get_file():
    """
    Get file from s3 interface
    """
    args = request.args
    file_name = args.get("name")
    tmp = tempfile.NamedTemporaryFile()
    try:
        image = s3_interface.get_file(file_name, bucket, tmp)
    except FileNotFoundError:
        return (
            jsonify(
                {
                    "error": "File not Found",
                }
            ),
            404,
        )
    else:
        return send_file(image, mimetype=mimetypes.guess_type(file_name)[0])


if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT)
