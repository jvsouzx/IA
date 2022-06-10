# Simple Reflex Vacuum Cleaner Agent
  Trabalho realizado para a disciplina de Inteligência Artificial, onde o objetivo é criar um agente reativo simples para o ambiente do aspirador de pó.

## Environment
  O ambiente foi representado por uma classe onde é atribuído um valor aleaório 0 ou 1 ao local A ou B, sendo 0 representando limpo e 1 sujo.
  ```
  self.localCondition = {'A': '0', 'B': '0'}
  self.localCondition['A'] = random.randint(0, 1)
  self.localCondition['B'] = random.randint(0, 1)
  ```

## Agent
  Foi também utilizada uma classe para representar o agente.
  ```
  class ReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print('Condição:',Environment.localCondition)
        vacuumPos = random.choice('AB')
        score = 0 
        print('Começando em ' + vacuumPos)

        for i in range(5):
            if vacuumPos == 'A':

                if Environment.localCondition['A'] == 1:
                    print('A está sujo, limpando A!')
                    Environment.localCondition['A'] = 0
                    score += 1
                else:
                    print('A está limpo, movendo para B!')
                    vacuumPos = 'B'
                    score -= 1

            elif vacuumPos == 'B':

                if Environment.localCondition['B'] == 1:
                    print('B está sujo, limpando B!')
                    Environment.localCondition['B'] = 0
                    score += 1
                else:
                    print('B está limpo, movendo para A!')
                    vacuumPos = 'A'
                    score -= 1
                    
        print('Pontuação:', score)
  ```
  O agente funciona da seguinte maneira, para começar é atribuído um valor randômico para a posição inicial, após é feita a verificação se o local está sujo, se estiver sujo o agente limpa, senão se move para outro local. O agente performa essas ações por 5 ciclos.

## Score Measurement
  Foi implementada uma medida de pontuação funcionando da seguinte maneira: Quando um local sujo é limpo é adicionado 1 à pontuação, quando o agente vai para um local já limpo é retirado 1 da pontuação.
  
## Results

| Condition A | Condition B | Start | Score |
|--- |--- |--- |--- |
| 1 | 1 | A | -1 |
| 1 | 1 | B | -1 |
| 1 | 0 | A | -3 |
| 1 | 0 | B | -3 | 
| 0 | 1 | A | -3 | 
| 0 | 1 | B | -3 |
| 0 | 0 | A | -5 | 
| 0 | 0 | B | -5 | 
