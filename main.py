import requests
import os
import zipfile

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

    if not os.path.exists(zip_path):
        try:
            res = requests.get(url)
        except Exception as e:
            print(f"main: requisição falhou com erro '{e}'")
            exit(1)

        if res.status_code != 200:
            print(f"main: requisição falhou com status '{res.status_code}'")
            exit(2)

        if len(res.text) == 0:
            print(f"main: resposta veio vázia")
            exit(3)
        
        try:
            zip_file = open(zip_path, "bw+")
        except:
            print(f"main: arquivo '{zip_path}' não abriu")
            exit(4)
        
        try:
            zip_file.write(res.content)
        except:
            zip_file.close()
            print(f"main: arquivo '{zip_path}' não escreveu")
            exit(5)
        
        zip_file.close()

        print(f"main: arquivo '{zip_path}' criado com sucesso!")
    else:
        print(f"main: pulando etapa, pois arquivo '{zip_path}' já existe")

    if not os.path.exists(file_path) and not os.path.exists(file_repath):
        try:
            zip_file = zipfile.ZipFile(zip_path, "r")
            zip_file.extractall(data_path)
        except:
            print("main: arquivo '{zip_path}' não extraiu")
            exit(6)

        print(f"main: arquivo '{zip_path}' extraído com sucesso!")
    else:
        print(f"main: pulando etapa, pois arquivo '{file_path}' já foi extraído")

    if not os.path.exists(file_repath):
        try:
            os.rename(file_path, file_repath)
        except:
            print(f"main: arquivo '{file_path}' falhou ao ser renomeado")
            exit(7)

        print(f"main: arquivo '{file_path}' renomeado com sucesso!")
    else:
        print(f"main: pulando etapa, pois arquivo '{file_path}' já foi renomeado")