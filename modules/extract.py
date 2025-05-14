import requests
import os
import zipfile
from typing import Optional, Union


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


def get_data(file_path:str, skip_first:bool=False) -> Union[Exception, list]:
    """
    Extrai dados em formato de matrix de arquivo csv em caminho 'file_path'.
    Se 'skip_first' for 'True' então a primeira linha será ignorada (por ser a linha das colunas).
    """

    try:
        file = open(file_path, "r")
    except:
        return Exception(f"extract.get_data: arquivo '{file_path}' falhou a abrir")

    try:
        fileread = file.read()
    except:
        file.close()
        return Exception(f"extract.get_data: arquivo '{file_path}' falhou a ser lido")

    file.close()

    rows: list[list] = []

    print("extract.get_data: extraindo ...")

    for n, row in enumerate(fileread.split('\n')):
        if skip_first and n == 0:
            continue

        columns = row.split(',')

        if len(columns) != 13:
            print(f"extract.get_data: linha '{n + 1}' mal-formada")
            continue

        rows.append(columns)

    print("extract.get_data: extração completa!")
    
    return rows


def download_hdi(hdi_path:str) -> Optional[Exception]:
    """
    Baixa informações de índice de desenvolvimento humano 
    dos vários países e põe em arquivo 'hdi_path'.
    """

    url = "https://raw.githubusercontent.com/openwashdata/worldhdi/main/inst/extdata/worldhdi.csv"

    if not os.path.exists(hdi_path):
        try:
            res = requests.get(url)
        except Exception as e:
            return Exception(f"extract.download_hdi: erro '{e}'") 

        if res.status_code != 200:
            return Exception(f"extract.download_hdi: requisição falhou com status '{res.status_code}'")

        if len(res.text) == 0:
            return Exception(f"extract.download_hdi: resposta veio vázia")
        
        try:
            zip_file = open(hdi_path, "w+")
        except:
            return Exception(f"extract.download_hdi: arquivo '{hdi_path}' não abriu")
        
        try:
            zip_file.write(res.text)
        except:
            zip_file.close()
            return Exception(f"extract.download_hdi: arquivo '{hdi_path}' não escreveu")
        
        zip_file.close()

        print(f"extract.download_hdi: arquivo '{hdi_path}' criado com sucesso!")
    else:
        print(f"extract.download_hdi: pulando etapa, pois arquivo '{hdi_path}' já existe")

    return None


def get_hdi(file_path:str, skip_first:bool=False) -> Union[Exception, list]:
    """
    Extrai dados de 'indice de desenvolvimento humano' em formato de matrix de arquivo csv 
    em caminho 'file_path'. Se 'skip_first' for 'True' então a primeira linha será ignorada 
    (por ser a linha das colunas).
    """

    try:
        file = open(file_path, "r")
    except:
        return Exception(f"extract.get_hdi: arquivo '{file_path}' falhou a abrir")

    try:
        fileread = file.read()
    except:
        file.close()
        return Exception(f"extract.get_hdi: arquivo '{file_path}' falhou a ser lido")

    file.close()

    rows: list[list] = []

    print("extract.get_hdi: extraindo ...")

    for n, row in enumerate(fileread.split('\n')):
        if skip_first and n == 0:
            continue

        columns = row.split(',')

        if len(columns) != 17:
            print(f"extract.get_hdi: linha '{n + 1}' mal-formada")
            continue

        rows.append([columns[1], columns[9]])

    print("extract.get_hdi: extração completa!")
    
    return rows
