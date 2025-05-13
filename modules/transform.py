
def prepare_load(data:list[list]) -> list[tuple]:
    """
    Esta função prepara os dados para serem carregadas no banco de dados; 
    sendo perfeita para validação, transformação e correção de dados.
    """

    prepared_rows:list[tuple] = []

    for n, row in enumerate(data):
        if len(row) != 13:
            print(f"transform.prepare_load: linha '{n}' mal-formada")
            continue

        if row[2] == 'Female':
            gender = 'F'
        elif row[2] == 'Male':
            gender = 'M'
        else:
            print(f"transform.prepare_load: gênero '{row[2]}' em linha '{n}' é inválido")
            continue

        if row[3] == 'High School':
            academic_level = 'H'
        elif row[3] == 'Undergraduate':
            academic_level = 'U'
        elif row[3] == 'Graduate':
            academic_level = 'G'
        else:
            print(f"transform.prepare_load: nível acadêmico '{row[3]}' em linha '{n}' é inválido")
            continue

        if row[7] == 'No':
            affects_studies = False
        elif row[7] == 'Yes':
            affects_studies = True
        else:
            msg = f"transform.prepare_load: coluna 'afeta performance acadêmica' " + \
                f"veio com valor '{row[7]}' em linha '{n}' que é inválido"

            print(msg)
            continue

        if row[10] == 'Single':
            relationship_status = 'S'
        elif row[10] == 'In Relationship':
            relationship_status = 'R'
        elif row[10] == 'Complicated':
            relationship_status = 'C'
        else:
            print(f"transform.prepare_load: status de relacionamento '{row[10]}' em linha '{n}' é inválido")
            continue

        survey_id = row[0]
        age = row[1]
        country = row[4]
        average_daily_usage = row[5]
        most_used_platform = row[6]
        sleeping_hours = row[8]
        mental_health_score = row[9]
        conflict_over_social_media = row[11]
        addicted_score = row[12]

        prepared_row = (
            survey_id,
            age,
            gender,
            academic_level,
            country,
            average_daily_usage,
            most_used_platform,
            affects_studies,
            sleeping_hours,
            mental_health_score,
            relationship_status,
            conflict_over_social_media,
            addicted_score,
        )

        prepared_rows.append(prepared_row)

    return prepared_rows
    