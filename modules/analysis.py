import sqlite3
from matplotlib_terminal import plt as plotter
from typing import Union

def get_row_count(conn:sqlite3.Connection) -> Union[Exception, tuple]:
    """
    Função destinada a visualizar quantidade de linhas no banco - 
    perfeito para ter certeza se dado já foi inserido.

    #funcao_atomica
    """

    query = """
    select count(id) from surveyees;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchone()[0]
    except Exception as e:
        return Exception(f"analysis.get_row_count: {e}")

    return res

def get_all(conn:sqlite3.Connection) -> Union[Exception, tuple]:
    """
    Função retorna todas as entradas do banco ou excessão.

    #funcao_atomica
    """

    query = """
    select * from surveyees;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.get_all: {e}")

    return res


def group_addiction_by_age(conn:sqlite3.Connection) -> Union[Exception, list]:
    """
    Função retorna agregado de vício médio por faixa etária ou excessão.

    #funcao_atomica
    """

    query = """
    select age, avg(addicted_score) as average_addicted_score from surveyees group by age;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_by_age: {e}")

    return res


def group_addiction_by_country(conn:sqlite3.Connection) -> Union[Exception, list]:
    """
    Função retorna agregado de vício médio por país ou excessão.

    #funcao_atomica
    """

    query = """
    select country, avg(addicted_score) as average_addicted_score from surveyees group by country;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_by_age: {e}")

    return res


def display_addiction_by_age(data:list[tuple]):
    """
    Mostra gráfico no terminal.

    #todo:fazer-funcionar
    """

    plotter.plot(data, lw=3)
    plotter.title("Relação entre idade e vício com redes sociais")
    plotter.show("block")