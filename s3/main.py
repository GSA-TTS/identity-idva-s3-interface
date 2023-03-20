import tempfile
import mimetypes
from flask import Flask, jsonify, request, send_file
from s3 import s3_interface
from s3 import settings

s3_clients = s3_interface.get_clients(settings.S3_CREDENTIALS)

app = Flask(__name__)


@app.route("/<service_id>", methods=["GET", "DELETE"])
def s3_file(service_id):
    """
    Get or Delete file from s3 interface
    """

    if not service_id in settings.S3_CREDENTIALS:
        return (
            jsonify(
                {
                    "error": "S3 Service not Found",
                }
            ),
            404,
        )

    bucket = settings.S3_CREDENTIALS[service_id]["bucket"]
    s3_client = s3_clients[service_id]

    args = request.args
    file_name = args.get("file")

    try:
        if request.method == "GET":
            tmp = tempfile.NamedTemporaryFile()
            image = s3_interface.get_file(s3_client, bucket, file_name, tmp)
            return send_file(image, mimetype=mimetypes.guess_type(file_name)[0])
        else:
            s3_interface.delete_file(s3_client, bucket, file_name)
            return (
                jsonify(
                    {
                        "success": "True",
                    }
                ),
                200,
            )
    except FileNotFoundError:
        return (
            jsonify(
                {
                    "error": "File not Found",
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT)
