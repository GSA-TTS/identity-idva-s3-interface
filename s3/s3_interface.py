import base64
import tempfile


class S3Interface:

    def get_file(key, bucket):
        """
        return specific file in base64 format from bucket to be stored in temp local file
        """
        tmp = tempfile.NamedTemporaryFile()

        # save file
        try:
            with open(tmp.name, 'wb') as f:
                bucket.download_fileobj(key, f)
        except:
            raise FileNotFoundError

        # read and convert file to base64
        with open(tmp.name, 'rb') as f:
            b64 = base64.b64encode(f.read())

        return b64.decode('utf-8')
