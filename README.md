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

5- datacleaning (Fase muito importamte no Machine learning)

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


6- divisão das variaveis em teste e treino 

20% da amostra é para testes

7- treino do modelo

modelo 1- regressão lienar 
Bom para capturar tendencias globais e relaçoes diretas

modelo 2- random forest
Utilizado pelo facto de ter a capacidade de captura não linear. 
Identifica o que a linha reta ignora.
8- aavaliação 

O modelo foi treinado e comparado entre diferentes modelos , como Regressão Logística e Random Forest. Avaliando o seu desenpanho de acordo com as metricas : accuracy, precision, F1-score, sendo o melhor modelo selecionado com base no melhor equilibrio entre o desempenho preditivo e interpretabilidade.

3. Comparações & Resultados

                Model      RMSE       MAE        R2

0  Linear Regressions  0.051047  0.038190  0.957667
1       Random Forest  0.044366  0.034176  0.968023

De acordo com os resultados obtidos o modelo "rabdom" forest" apresenta um R2 superior em comparação com o do modelo da regressão linear. O mesmo acontece em relação aos parametros do erro, em todas as  emtricas o Random forest demonstra um menor erro e uma maior precisão.


Anlise do grafico: 

- linhas diagonais muito proximas, pouco ruido
- o modelo consegue esta a conseguir prever o risck score quase perfeito (R2 = 96%)

- espaços em branco entre as linhas são valores de risco que o modelo raramente preve, devido a combinação de caracteristicas que fazem no saltar de um nivel para outro.
 

4. Conclusões 

nota- o excel gerado no fianl apenas contem os 20% os dados de teste

Analisando os dados do novo excel, conseguimos ver que o random forest tem metricas globais melhores, mas que a disputa é equilibrada. 

a regressão linear em 45% das vezes realmente granha reraltivamente ao outro modelo, e assim olhando pleas linhas podemos ter a sensação que o melhro é o modelo da regressão lienar.

Em suma o modelo random forest é o melhor para utilizar neste contexto , pois é mais preciso a difentificar quem são os clientes de ALto risco ( > prejuizo) e os de baixo risco. Enquanto a regressão linear apenas funciona bem para valores medios, falhando em casos especiais/ extremos.

Utilizou -se o k-Means para verificar o  realdesempenho e provar que não é uniforme. 

Risco Baixo - dominado pelo random forest.
identifica muito bem clientes saudaveis.

Risco Médio- regressão lienar é competitiva e chega a ganhar com 45% dos casos gerais. demonstra a qualidade do modelo que para um nivel "normal/comum" o modelo simples basta.

Risco ALto- dominado pelo random forest. 
grupo critico, onde o modelo deteta a combinação das caracteristicas que aumentam exponencialmente a gravidade, algo que o modelo lienear não destaca.


Com isto, afirmamos que embora a regressão linear seja robusta em caso medios, o Random forest é destacado e selecionado como o modelo final. devido a sua superioridade de precisão e deteção em casos extremos (baixos e altos), garantindo que a seguradora identifique de forma corerta os casos que causam maior risco financeiro.


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


Clusterin? 
Tecnica de aprendizagem não supervisionaa.
recebe dados e tenat encontrar grupos que se relacionem entre si, no nosso caso vai segmentar clientes  pelo perfil de risco mais adequanto ou semelhate tendo em conta a caracterização dos parametros sem intervenção humana.

-> algoritmo K-Means é o mais comum.
Calcula "distancia" ( diferença ) entre pontos, logo temos de colcar tudo na mesma escala
- Distancia Euclidiana( em linha reta entre os pontos num grafico)

-> Metodo do Cotovelo( elbow Method)
Pergunta " quantos grupos devo criar ?" , sera que é o numero que melhor representa a realidade dos dados?
Valida se o nº de grupos(k=x) faz sentido matematicamente

- Medição da inércia 
o que é  a inercia ? - propriedade da matéria que faz com que um corpo resista a mudanças no seu estado de movimento ou repouso. Neste caso a inércia vai dizer-nos a que distancia os clientes se encontram do seu grupo,
- Quantos mais grupos crias menor é a inércia, grupos com pouca distancia entre eles,

- Para verificarmos se temos um numero de grupos correto ajuda se desenharmos um grafico da inercia e o compararmos com o numero de grupos.
Inicialmente a curva desce rapidamente e depois estabiliza, o ponto onde a descida abranda e faz uma curva "cotovelo" é o numero ideal de grupos. 



```bash

Bibliografia : 
- https://stackoverflow.com/questions/51237635/difference-between-standard-scaler-and-minmaxscaler
- https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/
- https://www.datacamp.com/pt/tutorial/sklearn-linear-regression
- https://www.geeksforgeeks.org/machine-learning/clustering-in-machine-learning/

```
