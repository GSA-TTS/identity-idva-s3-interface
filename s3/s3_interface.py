
class S3Interface:

    def get_file(key, bucket, tmp):
        """
        return specific file in base64 format from bucket to be stored in temp local file
        """

        # save file
        try:
            with open(tmp.name, 'wb') as f:
                bucket.download_fileobj(key, f)
        except:
            raise FileNotFoundError

        return tmp.name
