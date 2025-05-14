# Análise de vício por uso de redes sociais

## Introdução

Este projeto estuda a taxa de vício de uso de redes sociais a medida que demonstra meus conhecimentos nas melhores práticas em programação com Python e ETL (extract-traform-load).

Escolhi este tema por causa de sua relevância social na atualidade, sendo muito importante para gerar consciência sobre o problema com o intuito de embasar possíveis soluções miradas as faixas etárias.

A fonte deste dado se encontra em 'https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships', mais precisamente, você pode baixar o arquivo com o _link_ 'https://www.kaggle.com/api/v1/datasets/download/adilshamim8/social-media-addiction-vs-relationships'.

Esta fonte de dados inclui informações sobre:
id do estudante; idade; genêro; nível acadêmico; país; uso médio diário em horas; plataforma mais usada; afeto em performance acadêmica; horas dormidas por noite; nota de saúde mental; status de relacionamento; conflitos sobre mídias sociais; e, nota de vício geral.

## Extração

A extração dos dados envolveu o baixamento do arquivo usando a biblioteca 'requests';
a extração (literalmente) do arquivo '.zip' em '.csv' usando 'zipfile';
transformações de colunas para as conveniências usadas neste projeto (ex.: 'High School' para 'H');
a secessão do arquivo '.csv' usando '\n' e ',' para transformá-lo em uma lista no Python de linhas e colunas;
finalmente, o carregamento no banco de dados Sqlite.

## Consultas

Apresentei cinco consultas:
o primeiro, agreguei por idade;
o segundo, por país;
o terceiro, por intervalo de idade 
(estão presente duas faixas etárias);
o quarto, por intervalo de uso médio 
de redes sociais;
e, o quinto, por tipo de relacionamento.

Tive interesse nestas consultas, pois elas demonstram as 
relações entre o vício em redes sociais e outros fatores como idade, 
país e relacionamento. 

Relativo as visualizações de idade - separei dois tipos diferentes; 
o primeiro, por idades absolutas, enquanto, o segundo, por intervalos - 
dividir os dados desta forma ajuda na visualização.

A tabela 'Vício por país' demonstrou que a taxa de vício é bem espalhada
(quanto a níveis de desenvolvimento humano), necessitando investigar mais a 
fundo cada situação por região.

A apresentação da relação entre vício e tempo de uso foi óbvia, 
portanto resumo minhas palavras.

Finalmente, a tabela de 'Vício por tipo de relacionamento' demonstrou que 
a relação 'complexa' possui índices levemente maiores de pessoas vicíadas;
seguido por 'solteiro'; e, finalmente, 'em relacionamento'.

Todas estas tabelas ajudam a descrever melhor os dados de modo a 
promover compreensão sobre a problemática - minha favorita foi a ultima.

## Ademais

Neste projeto eu pratiquei o uso de uma arquitetura modular orientada a funções atômicas (funções que se executadas da segunda vez possuem o mesmo efeito que a primeira - ótimas para garantir consistência no estado do programa) com o objetivo de possuir um gerenciamento robusto de possíveis excessões. 

O agrupamento dos dados, foi uma etapa muito interessante para mim, principalmente a parte de dividir os dados em intervalos categóricos. Organizar estes, em formato de tabela no terminal também foi um ponto significante!

Um dos objetivos deste projeto também foi o uso da biblioteca 'logging' para criação de _logs_ - usado em programs de rotinas (_jobs_); porém, devido ao prazo, esta melhoria não coube. Outro ramo, que este projeto poderia ter explorado era o de _web-scrapping_ - algo que gosto bastante; sendo que, não consegui encaixar neste projeto.

Para concluir, sinto que, embora este estudo de caso tenha sido mais demonstrativo do que exploratório, aprendi muito ao realiza-lo; e, certamente, este projeto me servirá de inspiração para outros que virão.
