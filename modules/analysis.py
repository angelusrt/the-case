import sqlite3
from typing import Union


def get_row_count(conn:sqlite3.Connection) -> Union[Exception, tuple]:
    """
    Função destinada a visualizar quantidade de linhas no banco - 
    perfeito para ter certeza se dado já foi inserido.

    #funcao_atomica
    """

    query = """
    SELECT COUNT(id) FROM surveyees;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchone()[0]
    except Exception as e:
        return Exception(f"analysis.get_row_count: {e}")

    return res


def get_all(conn:sqlite3.Connection) -> Union[Exception, list]:
    """
    Função retorna todas as entradas do banco ou excessão.

    #funcao_atomica
    """

    query = """
    SELECT * FROM surveyees;
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
    SELECT age, AVG(addicted_score) AS average_addicted_score 
    FROM surveyees GROUP BY age;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_by_age: {e}")

    return res


def show_addiction_by_age(data:list):
    """
    Apresenta os dados de 'group_by_age'
    no terminal, incluindo descrição.
    """

    print("Tabela 1.0: Vício por idade")
    print("==")
    print(f"{'Idade,':<7}{'Vício':>5}")

    for row in data:
        column0 = str(row[0]) + ","
        print(f"{column0:<7}{row[1]:.2f}")

    print("==")
    print("Esta tabela demonstra uma leve tendência ")
    print("de vício a mais em adolescentes do que ")
    print("em jovem-adultos")
    print()


def group_addiction_by_country(conn:sqlite3.Connection) -> Union[Exception, list]:
    """
    Função retorna agregado de vício médio por país ou excessão.

    #funcao_atomica
    """

    query = """
    SELECT country, AVG(addicted_score) AS average_addicted_score 
    FROM surveyees 
    GROUP BY country 
    ORDER BY average_addicted_score ASC;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_addiction_by_country: {e}")

    return res


def show_addiction_by_country(data:list):
    """
    Apresenta os dados de 'group_addiction_by_country'
    no terminal, incluindo descrição.
    """

    print("Tabela 1.1: Vício por país")
    print("==")
    print(f"{'País,':<18}{'Vício'}")

    for row in data:
        column0 = str(row[0]) + ","
        print(f"{column0:<18}{row[1]:.2f}")

    print("==")
    print("Esta tabela demonstra uma situação ")
    print("multi-facetada de vício por país")
    print()


def group_addiction_by_age_range(conn:sqlite3.Connection) -> Union[Exception, list]:
    """
    Função retorna agregado de vício médio por intervalos 
    de faixa etária ou excessão.

    #funcao_atomica
    """

    query = """
    SELECT 
        age_groups.age_range AS [score range],
        AVG(s.addicted_score) AS average_addicted_score
    FROM (
        SELECT 
            id,
            CASE
                WHEN age BETWEEN 0 AND 9 THEN '0-9'
                WHEN age BETWEEN 10 AND 19 THEN '10-19'
                WHEN age BETWEEN 20 AND 29 THEN '20-29'
                ELSE '30-100'
            END AS age_range
        FROM surveyees
    ) AS age_groups
    JOIN surveyees s ON s.id = age_groups.id
    GROUP BY age_groups.age_range;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_addiction_by_age_range: {e}")

    return res


def show_addiction_by_age_range(data:list):
    """
    Apresenta os dados de 'group_addiction_by_age_range'
    no terminal, incluindo descrição.
    """

    print("Tabela 1.2: Vício por intervalo de idade")
    print("==")
    print(f"{'Int. Idade,':<15}{'Vício':>5}")

    for row in data:
        column0 = str(row[0]) + ","
        print(f"{column0:<15}{row[1]:.2f}")

    print("==")
    print("Esta tabela demonstra a leve tendência ")
    print("de vício em adolescentes melhor ")
    print("(apesar que podiam haver mais dados).")
    print()


def group_addiction_by_social_media_usage(conn:sqlite3.Connection) -> Union[Exception, list]:
    """
    Função retorna agregado de vício médio por intervalos 
    de uso médio de redes sociais ou excessão.

    #funcao_atomica
    """

    query = """
    SELECT 
        usage_groups.usage_range AS [score range],
        AVG(s.addicted_score) AS average_addicted_score
    FROM (
        SELECT 
            id,
            CASE
                WHEN average_daily_usage BETWEEN 0 AND 3 THEN '0-3'
                WHEN average_daily_usage BETWEEN 4 AND 6 THEN '4-6'
                ELSE '7-10'
            END AS usage_range
        FROM surveyees
    ) AS usage_groups
    JOIN surveyees s ON s.id = usage_groups.id
    GROUP BY usage_groups.usage_range;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_addiction_by_social_media_usage: {e}")

    return res


def show_addiction_by_social_media_usage(data:list):
    """
    Apresenta os dados de 'group_addiction_by_social_media_usage'
    no terminal, incluindo descrição.
    """

    print("Tabela 1.3: Vício por intervalo ")
    print("de uso médio de mídias em horas")
    print("==")
    print(f"{'Int. de Uso,':<15}{'Vício':>5}")

    for row in data:
        column0 = str(row[0]) + ","
        print(f"{column0:<15}{row[1]:.2f}")

    print("==")
    print("Esta tabela demonstra uma correlação ")
    print("entre uso prolongado de redes sociais ")
    print("e vício.")
    print()


def group_addiction_by_relationship_status(conn:sqlite3.Connection) \
    -> Union[Exception, list]:
    """
    Função retorna agregado de vício médio por tipos de 
    status de relacionamento (estatística descritiva 
    qualitativa nominal) ou excessão.

    #funcao_atomica
    """

    query = """
    SELECT 
        relationship_status,
        AVG(addicted_score) AS average_addicted_score
    FROM surveyees 
    GROUP BY relationship_status 
    ORDER BY average_addicted_score ASC;
    """

    try:
        cursor = conn.cursor()

        cursor.execute(query)
        res = cursor.fetchall()
    except Exception as e:
        return Exception(f"analysis.group_addiction_by_relationship_status: {e}")

    return res


def show_addiction_by_relationship_status(data:list):
    """
    Apresenta os dados de 'group_addiction_by_relationship_status'
    no terminal, incluindo descrição.
    """

    print("Tabela 1.4: Vício por tipo ")
    print("de relacionamento")
    print("==")
    print(f"{'Relacionamento,':<20}{'Vício':>5}")

    for row in data:
        status = "Complexo"

        if row[0] == 'R':
            status = "Em Relacionamento"
        elif row[0] == 'S':
            status = "Solteiro"
        elif row[0] != 'C':
            status = "Outros"

        column0 = status + ","
        print(f"{column0:<20}{row[1]:.2f}")

    print("==")
    print("Esta tabela demonstra uma correlação ")
    print("(levemente maior) entre relacionamentos ")
    print("'complexos' e vício em redes sociais.")
    print()
