import requests
import os
import zipfile
from typing import Optional 


def download_zip_file(url:str, zip_path:str) -> Optional[Exception]:
    """
    Baixa arquivo binário localizado na url 'url' e põe em arquivo 'zip_path'.
    Função pode retornar excessão.

    #funcao_atomica
    """

    if not os.path.exists(zip_path):
        try:
            res = requests.get(url)
        except Exception as e:
            return Exception(f"extract.download_zip_file: requisição falhou com erro '{e}'")

        if res.status_code != 200:
            return Exception(f"extract.download_zip_file: requisição falhou com status '{res.status_code}'")

        if len(res.text) == 0:
            return Exception(f"extract.download_zip_file: resposta veio vázia")
        
        try:
            zip_file = open(zip_path, "bw+")
        except:
            return Exception(f"extract.download_zip_file: arquivo '{zip_path}' não abriu")
        
        try:
            zip_file.write(res.content)
        except:
            zip_file.close()
            return Exception(f"extract.download_zip_file: arquivo '{zip_path}' não escreveu")
        
        zip_file.close()

        print(f"extract.download_zip_file: arquivo '{zip_path}' criado com sucesso!")
    else:
        print(f"extract.download_zip_file: pulando etapa, pois arquivo '{zip_path}' já existe")

    return None


def unzip_zip_file(zip_path:str, folder:str, file_path:str, file_repath:str) -> Optional[Exception]:
    """
    Função extrai arquivo '.zip' e renomea arquivo extraído.
    Funcão pode retornar excessão.

    #funcao_atomica
    """

    if not os.path.exists(file_path) and not os.path.exists(file_repath):
        try:
            zip_file = zipfile.ZipFile(zip_path, "r")
            zip_file.extractall(folder)
        except:
            return Exception("extract.unzip_zip_file: arquivo '{zip_path}' não extraiu")

        print(f"extract.unzip_zip_file: arquivo '{zip_path}' extraído com sucesso!")
    else:
        print(f"extract.unzip_zip_file: pulando etapa, pois arquivo '{file_path}' já foi extraído")

    if not os.path.exists(file_repath):
        try:
            os.rename(file_path, file_repath)
        except:
            return Exception(f"extract.unzip_zip_file: arquivo '{file_path}' falhou ao ser renomeado")

        print(f"extract.unzip_zip_file: arquivo '{file_path}' renomeado com sucesso!")
    else:
        print(f"extract.unzip_zip_file: pulando etapa, pois arquivo '{file_path}' já foi renomeado")

    return None