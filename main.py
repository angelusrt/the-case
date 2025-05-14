import sqlite3
import os
from modules import extract, loading, transform, analysis

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

    row_count = analysis.get_row_count(connection)

    if isinstance(row_count, Exception):
        connection.close()
        print(row_count)
        exit(6)

    if row_count == 0:
        for n, row in enumerate(transformed_data):
            load_error = loading.load_surveyee(connection, row)

            if load_error is not None:
                print(load_error)
                continue

            connection.commit()
    else:
        print(f"main: pulando etapa - dados já carregados em banco de dados ('{row_count}' linhas)")

    age_groups = analysis.group_addiction_by_age(connection)

    if isinstance(age_groups, Exception):
        connection.close()
        print(age_groups)
        exit(7)

    print(f"main::analysis.group_addiction_by_age: '{age_groups}'")

    country_groups = analysis.group_addiction_by_country(connection)

    if isinstance(country_groups, Exception):
        connection.close()
        print(country_groups)
        exit(8)

    print(f"main::analysis.group_addiction_by_country: '{country_groups}'")

    connection.close()
