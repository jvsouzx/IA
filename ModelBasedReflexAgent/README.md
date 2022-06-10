# Model Based Reflex Agent
Agente Reativo Baseado em Modelo feito para a disciplina de Inteligência Artificial

## Environment
O ambiente foi declarado como um dicionário, ou seja, um local está associado ao seu respectivo estado.
```
localCondition = {'A': '', 'B': ''}
```
O local pode estar relacionado a um dos dois estados: 'sujo' ou 'limpo'

Para iniciar o estado dos locais é utilizada uma função randômica.
```
def initLocalCondition(localCondition, condition):
    localCondition['A'] = random.choice(condition)
    localCondition['B'] = random.choice(condition)
```

## Agent

Foi implementada uma classe para reprentar o agente: ```class VacuumAgent():```
Para reprenstar a movimentação do agente foi declarada a função ```movement```
A função ```movement``` verifica o estado anterior do locail, se o local não foi limpo ele faz o procedimento para limpar senão ele verifica o outro local, se ambos estiverem limpos o agente termina sua execução.
O trecho de código que executa tal verificação é apresentado abaixo:
```

if self.vacuumPos == 'A' and (self.state['A'] != 'limpo' or self.state['B'] != 'limpo'):
    print('Aspirador está em A')
    
    if localCondition['A'] == 'sujo':
        print('A está sujo, limpando A!')
        localCondition['A'] = 'limpo'
        self.state['A'] = 'limpo'
        self.score += 2
    else:
        print('A está limpo')
        self.vacuumPos = 'B'
        self.state['A'] = 'limpo'
        self.score -= 1
                
elif self.vacuumPos == 'B' and (self.state['A'] != 'limpo' or self.state['B'] != 'limpo'):
     print('Aspirador está em B')

     if localCondition['B'] == 'sujo':
        print('B está sujo, limpando B!')
        localCondition['B'] = 'limpo'
        self.state['B'] = 'limpo'
        self.score += 2
     else:
        print('B está limpo')
        self.vacuumPos = 'A'
        self.state['B'] = 'limpo'
        self.score -= 1
```
  
## Score Measurement
Para avaliar o desempenho do agente foi implementada uma função de pontuação onde é adicionado 2 pontos por local limpo e retirado 1 ponto por movimento.

## Results

| Condition A | Condition B | Start | Score |
|--- |--- |--- |--- |
| sujo | sujo | A | 3 |
| sujo | sujo | B | 3 |
| sujo | limpo | A | 0 |
| sujo | limpo | B | 1 | 
| limpo | sujo | A | 1 | 
| limpo | sujo | B | 0 |
| limpo | limpo | A | -2 | 
| limpo | limpo | B | -2 | 
