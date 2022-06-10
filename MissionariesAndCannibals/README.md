# Missionaries and Cannibals

Três missionarios e três canibais estão em um lado de um rio, juntamente com um barco que pode levar uma ou duas pessoas. Descubra um meio de fazer todos atravessarem o
rio sem deixar que um grupo de missionarios de um lado fique em número menor que o número de canibais nesse mesmo lado do rio.

## Formulação do Problema
- Estado inicial: 3 missionários, 3 canibais, 1 barco no lado de início e 0 missionários, 0 canibais e 0 barco do outro lado do rio.
- Teste de Objetivo: Verificar se existem 0 missionários, 0 canibais e 0 barco no lado de início do problema.
- Função Sucessora: 
    - ACTION(3,3,1) = {(2,2,0), (3,1,0), (3,2,0)} 
    - ACTION(2,2,0) = {(3,2,1)} 
    - ACTION(3,1,0) = {(3,2,1)} 
    - ACTION(3,2,1) = {(3,0,0)} 
    - ACTION(3,1,1) = {(1,1,0)} 
    - ACTION(1,1,0) = {(2,2,1)} 
    - ACTION(2,2,1) = {(0,2,0)} 
    - ACTION(0,2,0) = {(0,3,1)} 
    - ACTION(0,3,1) = {(0,1,0)} 
    - ACTION(0,1,0) = {(0,2,1), (1,1,1)}
    - ACTION(1,1,1) = {(0,0,0)} 
    - ACTION(0,2,1) = {(0,0,0)} 
- Função custo: Quantidade de passos para se chegar ao estado meta.

## Árvore de Estados

<div align="center">
<img src="https://user-images.githubusercontent.com/60747654/168285965-7ca2f531-2773-4fbd-b268-556795483e7b.png">
</div>

