import tempfile
import mimetypes
from flask import Flask, jsonify, request, send_file
from s3 import s3_interface
from s3 import settings

s3_clients = s3_interface.get_clients(settings.S3_CREDENTIALS)

app = Flask(__name__)


@app.route("/get/<vendor_id>/", methods=["GET"])
def get_file(vendor_id):
    """
    Get file from s3 interface
    """

    if not vendor_id in settings.S3_CREDENTIALS:
        return (
            jsonify(
                {
                    "error": "S3 Service not Found",
                }
            ),
            404,
        )

    bucket = settings.S3_CREDENTIALS[vendor_id]["bucket"]
    s3_client = s3_clients[vendor_id]

    args = request.args
    file_name = args.get("file")

    tmp = tempfile.NamedTemporaryFile()
    try:
        image = s3_interface.get_file(s3_client, file_name, bucket, tmp)
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
