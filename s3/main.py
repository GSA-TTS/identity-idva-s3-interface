import os
import boto3
from flask import Flask, jsonify, request
from s3.s3_interface import S3Interface
from s3 import settings

s3 = boto3.resource(
    's3',
    aws_access_key_id=settings.KEY_ID,
    aws_secret_access_key=settings.SECRET_KEY,
    region_name=settings.REGION
)
bucket = s3.Bucket(settings.BUCKET)

app = Flask(__name__)


@app.route("/get", methods=['GET'])
def get_file():
    """
    Get file from s3 interface
    """
    args = request.args
    file_name = args.get('name')
    try:
        image = S3Interface.get_file(file_name, bucket)
    except FileNotFoundError:
        return jsonify({"error": "File not Found", }), 404
    else:
        return image


if __name__ == "__main__":
    port = int(os.getenv("PORT", settings.PORT))
    app.run(host='0.0.0.0', port=port)
