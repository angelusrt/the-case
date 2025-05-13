import os
from modules import extract

url = "https://www.kaggle.com/api/v1/datasets/download/adilshamim8/social-media-addiction-vs-relationships"

data_path = "data"
zip_name = "social-media-addiction.zip"
zip_path = os.path.join(data_path, zip_name)

file_name = "Students Social Media Addiction.csv"
file_path = os.path.join(data_path, file_name)

file_rename = "social-media-addiction.csv"
file_repath = os.path.join(data_path, file_rename)


if __name__ == "__main__":
    os.makedirs(data_path, exist_ok=True)

    download_error = extract.download_zip_file(url, zip_path)

    if download_error is not None:
        print(download_error)
        exit(1)

    unzip_error = extract.unzip_zip_file(zip_path, data_path, file_path, file_repath)

    if unzip_error is not None:
        print(unzip_error)
        exit(2)