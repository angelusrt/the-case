import sqlite3
import os
from typing import Optional, Union


def init_database(folder_path:str) -> Union[Exception, sqlite3.Connection]:
    """
    Esta função cria o arquivo 'database.db' para as próximas consultas sqlite3.
    Retorna ou uma excessão ou a conexão com o banco, já estabelicida.

    #funcao_atomica
    """

    database_path = os.path.join(folder_path, "database.db")

    if not os.path.exists(database_path):
        try:
            database_file = open(database_path, "w+")
        except:
            return Exception(f"loading.init_database: arquivo '{database_path}' falhou ao ser aberto")
        
        print(f"loading.init_database: arquivo '{database_path}' criado")
        database_file.close()
    else:
        print(f"loading.init_database: pulando etapa, pois arquivo '{database_path}' já existe")
    
    conn = sqlite3.connect(database_path)

    print(f"loading.init_database: conexão estabelicida!")

    return conn


def create_surveyees(conn:sqlite3.Connection) -> Optional[Exception]:
    """
    Esta função cria a tabela de entrevistados - pode retornar excessão.

    #funcao_atomica
    """

    query = """
        create table if not exists surveyees (
            id integer primary key autoincrement not null unique,
            survey_id biginteger not null unique,
            age smallinteger not null,
            gender text check(gender in ('M', 'F')) not null default 'M',
            academic_level check(academic_level in ('H', 'U', 'G')) not null default 'H',
            country text not null default 'Brasil',
            average_daily_usage numeric not null,
            most_used_platform text not null,
            affects_academic_performance bool not null,
            sleeping_hours numeric not null,
            mental_health_score integer not null,
            relationship_status text check(relationship_status in ('S', 'R', 'C')) not null default 'S',
            conflicts_over_social_media integer not null default 0,
            addicted_score integer not null
        )
    """

    try:
        cursor = conn.cursor()
        cursor.execute(query)
    except Exception as e:
        return Exception(f"loading.create_surveyees: erro '{e}'")

    print("loading.create_surveyees: query realizada com sucesso!")
    return None


def load_surveyee(conn:sqlite3.Connection, row:tuple) -> Optional[Exception]:
    """
    Esta função carrega um participante por vez - pior para performance, 
    melhor para a conveniência e segurança.

    #funcao_atomica
    """

    query = f"""
    insert into surveyees (
        survey_id,
        age,
        gender,
        academic_level,
        country,
        average_daily_usage,
        most_used_platform,
        affects_academic_performance,
        sleeping_hours,
        mental_health_score,
        relationship_status,
        conflicts_over_social_media,
        addicted_score
    ) values (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """

    try:
        cursor = conn.cursor()
        cursor.execute(query, row)
    except Exception as e:
        return Exception(f"loading.load_surveyee: erro '{e}'")

    return None