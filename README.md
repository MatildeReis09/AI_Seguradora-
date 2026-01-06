# AI_Seguradora-

Duas possibilidades de risk score: 

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

Parametros a ter em conta para o calculo do risk score: 

