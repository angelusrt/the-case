import os
import sqlite3
from modules import extract, loading, transform

url = "https://www.kaggle.com/api/v1/datasets/download/adilshamim8/social-media-addiction-vs-relationships"

data_path = "data"
database_path = "database"

zip_name = "social-media-addiction.zip"
zip_path = os.path.join(data_path, zip_name)

file_name = "Students Social Media Addiction.csv"
file_path = os.path.join(data_path, file_name)

file_rename = "social-media-addiction.csv"
file_repath = os.path.join(data_path, file_rename)


if __name__ == "__main__":
    os.makedirs(data_path, exist_ok=True)
    os.makedirs(database_path, exist_ok=True)

    download_error = extract.download_zip_file(url, zip_path)

    if download_error is not None:
        print(download_error)
        exit(1)

    unzip_error = extract.unzip_zip_file(zip_path, data_path, file_path, file_repath)

    if unzip_error is not None:
        print(unzip_error)
        exit(2)

    data = extract.get_data(file_repath, True)

    if isinstance(data, Exception):
        print(data)
        exit(3)
    
    assert isinstance(data, list)

    transformed_data = transform.prepare_load(data)

    connection = loading.init_database(database_path)

    if isinstance(connection, Exception):
        print(connection)
        exit(4)

    assert isinstance(connection, sqlite3.Connection)

    create_error = loading.create_surveyees(connection)

    if create_error is not None:
        connection.close()
        print(create_error)
        exit(5)

    for n, row in enumerate(transformed_data):
        load_error = loading.load_surveyee(connection, row)

        if load_error is not None:
            print(load_error)
            exit(6)

        connection.close()
        exit(7)
    
    connection.commit()
    connection.close()