# AI_Seguradora-

Trabalho de Machine learning : Previsão do calculo do risck score

1. Dataset 

O conjuto de dados utilizado é composto por aproxiamdamente 10000 registos de clientes de uma seguradora, contendo todo o tipo de informações desde demograficas, a cínicas  e comportamentais.

Identificamos a variavel alvo como risck-score, indicando se o cliente pertence ou não a um grupo alto de risco.

2. Matodologia 

Para o calculo desta variavel, adota-se uma abordagem de aprendizagem supervisionada  para o previsão do risck score. 

O processo foi realizado por fases: 

    1- analise exploratoria dos dados 
    2- definição da variavel- alvo 

    Target - Risck_score ( continuo [ 0-100])
    variavel Y 

    A variavel -alvo ou Target é a componente central de um modelo. 
    É a variavel especifica que o modelo tenta prever ou explicar. Represneta a resposta que queremos que o modelo aprenda e preveja de um conjunto de dados.

    3- seleção de variaveis mais relevantes

    Variaveis X

    Age -> Variavel continua esatvel, com forte relação com o risco de saúde 
    smoker -> Variavel comportamental de risco
    chronical_disease_count -> "Resume" o estado de vida do cliente
    employment_status -> Reflete a esatbilidade socioeconomica e a capacidade de acesso a cuidades
    income -> Reflete o risco financeiro e o acesso à saúde

    4- Modelo 

    Regressão Logística ->interpretavel
    Random Forest -> modelo não lienar

    5- datacleaning 



    6- divisão das variaveis em teste e treino 
    7- treino do modelo
    8- aavaliação 

O modelo foi treinado e comparado entre diferentes modelos , como Regressão Logística e Random Forest. Avaliando o seu desenpanho de acordo com as metricas : accuracy, precision, F1-score, sendo o melhor modelo selecionado com base no melhor equilibrio entre o desempenho preditivo e interpretabilidade.

3. Comparações & Resultados

4. Conclusões 














(Variaveis escolhidas)
As variáveis explicativas selecionadas para o modelo de previsão do risk score incluem características demográficas (age), comportamentais (smoker) e históricas relacionadas com sinistros (index_gravidade, sinistralidade). Estas variáveis foram escolhidas por apresentarem forte relação teórica e empírica com o risco associado aos clientes. Variáveis que poderiam introduzir data leakage, como indicadores de rentabilidade futura, foram excluídas para garantir a robustez do modelo.




Duas possibilidades da divisao do risk score: 

1-3 ( nivel baixo, nivel medio, nivel alto): 
- injusto para quem esta no limite de um nivel,
- simplifica a tomada de decisão, 
- util quando os dados não teem diferenças subties,
- k= 3,
- maior variancia entre cada grupo, o que leva a pessoas diferentes serem colocadas no mesmo score, 
- menor risco de erro, 
- mais facil,
- menos preciso e pouco presonalizado

1-5 ( nivel muito baixo, nivel baixo, nivel medio, nivel alto , nivel muito alto): 
- permite identificar extremos,
- preços mais competitivos, personalizado e preciso,
- mais justo, pois evita que bons clientes paguem pelos maus, 
- isola melhor outliers,
- k= 5,  
- 5 grupos com uma variancia mais pequena entre eles, 
- maior risco de erro


Parametros ter em conta para o calculo do risk score: 
    -idade
    -smoker
    -frequencia alcool 
    -nº hospitalizações nos ultimos 3 anos
    -clain count (nº de sinistros)
    -dependentes ?
    -index_desease  ( dar importancia diferente as doenças)

-> Agrupar parametros, pode ser util
Assim em vez de dar 10 colunas diferentes (uma de cada doença), cria-se uma nova coluna doencas_index.   
cada doença = 1 , doenças cronicas = 2 e o valor do indice vai somando os valores, caso não tenha nada = 0 

O facto de ter muitas doenças é um fator forte e acumulativo de risco 


Clusterin? 
Tecnica de aprendizagem não supervisionaa.
recebe dados e tenat encontrar grupos que se relacionem entre si, no nosso caso vai segmentar clientes  pelo perfil de risco mais adequanto ou semelhate tendo em conta a caracterização dos parametros sem intervenção humana.

-> algoritmo K-Means é o mais comum.
Calcula "distancia" ( diferença ) entre pontos, logo temos de colcar tudo na mesma escala
- Distancia Euclidiana( em linha reta entre os pontos num grafico)

-> Metodo do Cotovelo( elbow Method)
Pergunta " quantos grupos devo criar ?" , sera que é o numero que melhor representa a realidade dos dados?
Valida se o nº de grupos(k=x) faz sentido matematicamente

- medição da inércia 
o que é  a inercia ? - propriedade da matéria que faz com que um corpo resista a mudanças no seu estado de movimento ou repouso. Neste caso a inércia vai dizer-nos a que distancia os clientes se encontram do seu grupo,
- Quantos mais grupos crias menor é a inércia, grupos com pouca distancia entre eles,

- Para verificarmos se temos um numero de grupos correto ajuda se desenharmos um grafico da inercia e o compararmos com o numero de grupos.
Inicialmente a curva desce rapidamente e depois estabiliza, o ponto onde a descida abranda e faz uma curva "cotovelo" é o numero ideal de grupos. 


Data cleaning ( Fase muito importamte no Machine learning ):

-> Tratamento de Valores nulos ( missing values)
ou preenchemos com "Unknown" , com o valor mais comum ou remove-se a coluna 
    -eleminação da coluna alccol, embora valiosa para o calculo por ter muitos valores em  falta não vai ser utilizado 
    cerca de 30% de dados em falta

-> Codigicação 
Converter parametros com variaveis de texto em numeros ( binarios ou ordinario ). uma vez que se vai medir a distancia tem de estar tudo na mesma forma

-> Normalização/Scaling ( importante para não haver decisões erradas)
colocar tudo na mesma escala (0-1), pois o k-Means calcula a distancia entre os pontos. colocar todos os parametros a falar a mesma lingua.

-> Min-Max Scaling 
todos os valores entre 0-1

-> Standard Scaling ( a usar)
trasforma os dados paar que a média seja 0 e o desvio padrao seja 1
" este parametro esta a quantos desvios da média?"
 bom quando há outliers ( provavel de acontecer neste caso por exemplo no parametro do "Income" e "hospitalizations") 


Parameltros usados realmente para o calculo: 
    'age',
    'smoker',
    'annual_medical_cost',
    'index_gravidade',
    'claims_count', 

atenção aos parametros 'annual_medical_cost' e claims_count , podem ser muito parecidos
Calculo da coreelação entre os dois parametros 
- Correlação nula (0.19) significa que não existe uma relação linear previsível entre duas variáveis
Pode se usar ambos para capturar as diferentes dimensões do risco. 
Se usasse só o custo anual, não se sabia a utilização do cliente.
Se usasse só a quantidade de claims, ignorava o impacto financeiro de doenças graves isoladas. 
- permite criar grupos mais precisos e detalhados 

- annul_medical_cost é um parametro de media ponderada, foi descartado 
calculo do 


Variaveis calculadas no excel 
- 

```bash

5. Bibliografia : 
- https://stackoverflow.com/questions/51237635/difference-between-standard-scaler-and-minmaxscaler

```
