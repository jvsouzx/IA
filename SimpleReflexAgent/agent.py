import random


class Environment(object):
    def __init__(self):
        # 0 indica limpo e 1 indica Sujo
        self.localCondition = {'A': '0', 'B': '0'}
        self.localCondition['A'] = random.randint(0, 1)
        self.localCondition['B'] = random.randint(0, 1)


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

L = Environment()
Vacuum = ReflexVacuumAgent(L)
