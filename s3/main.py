import os
from flask import Flask, request, send_file
from . import s3_interface

app = Flask(__name__)


@app.route("/list")
def list():
    contents = s3_interface.list_files()
    return str(contents)


@app.route("/get", methods=['GET'])
def get_file():
    args = request.args
    file_name = args.get('name')
    image = s3_interface.get_file(file_name)
    #return send_file(image, mimetype='image/jpeg')
    return image


@app.route("/delete", methods=['DELETE'])
def delete_file():
    args = request.args
    file_name = args.get('name')
    return s3_interface.delete_file(file_name)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
