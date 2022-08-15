import os
from flask import Flask, request, send_file
from . import s3_interface, settings
import tempfile

app = Flask(__name__)

@app.route("/list")
def list():
    contents = s3_interface.list_files(settings.BUCKET)
    return str(contents)

@app.route("/get-file", methods=['GET'])
def get_file():
    args = request.args
    file_name = args.get('name')
    tmp = tempfile.NamedTemporaryFile()
    image = s3_interface.get_file(file_name, settings.BUCKET, tmp)
    return send_file(image, mimetype='image/jpeg')


if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host='0.0.0.0', port=port)