# Análise de vício por uso de redes sociais

## Introdução

Este projeto estuda a taxa de vício de uso de redes sociais a medida que demonstra meus conhecimentos nas melhores práticas em programação com Python e ETL (extract-traform-load).

Escolhi este tema por causa de sua relevância social na atualidade, sendo muito importante para gerar consciência sobre o problema com o intuito a embasar possíveis soluções miradas as faixas etárias.

A fonte deste dado se encontra em 'https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships' mais precisamente, você pode baixar o arquivo com o link 'https://www.kaggle.com/api/v1/datasets/download/adilshamim8/social-media-addiction-vs-relationships'.

Esta fonte de dados inclui informações sobre:
id do estudante; idade; genêro; nível acadêmico; país; uso médio diário em horas; plataforma mais usada; afeto em performance acadêmica; horas dormidas por noite; nota de saúde mental; status de relacionamento; conflitos sobre mídias sociais; e, nota de vício geral.

## Extração

A extração dos dados envolveu o baixamento do arquivo usando a biblioteca 'requests';
a extração (literalmente) do arquivo '.zip' em '.csv' usando 'zipfile';
transformações de colunas para as conveniências usadas neste projeto (ex.: 'High School' para 'H');
a secessão do arquivo '.csv' usando '\n' e ',' para transformá-lo em uma lista no Python de linhas e colunas;
finalmente, o carregamento no banco de dados Sqlite.

## Consultas

Utilizei dois agrupamentos; um por idade e o outro por país.
Estes dois agrupamentos são utéis para visualizar tendências etárias 
e por desenvolvimento por país; portanto, sendo fundamentais na apuração 
da necessidade de uma tomada de decisão e na formação de decisões miradas a 
diferentes grupos.

## Ademais

Neste projeto eu pratiquei o uso de uma arquitetura modular orientada a funções atômicas (funções que se executadas da segunda vez possuem o mesmo efeito que a primeira - ótimas para garantir consistência no estado do programa) com o objetivo de possuir um gerênciamento robusto de possíveis excessões. 

Um dos objetivos deste projeto também foi o uso da biblioteca 'logging' para criação de _logs_ em programs de rotinas (_jobs_); porém, devido ao prazo, esta melhoria não coube.