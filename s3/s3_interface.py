import os

from PIL import Image


def get_file(key, bucket, tmp):
    """
    return specific file in base64 format from bucket to be stored in temp local file
    """
    filename = tmp.name

    # save file
    try:
        with open(tmp.name, "wb") as f:
            bucket.download_fileobj(key, f)
    except:
        raise FileNotFoundError

    # normalize image type
    try:
        tmp_path, _ = os.path.split(tmp.name)
        base_name = os.path.basename(key)
        file_name_no_ext = os.path.splitext(base_name)[0]
        filename = tmp_path + "/" + file_name_no_ext + ".jpeg"

        image = Image.open(tmp.name)
        image.save(filename)
    except:
        raise FileNotFoundError

    return filename
