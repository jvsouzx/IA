import random

class VacuumAgent():
    def __init__(self):
        self.vacuumPos = random.choice('AB')
        self.score = 0
        self.state = {'A':'', 'B':''}
        
    def movement(self, localCondition):
        for i in range(5):

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
                    
        print('Pontuação:', self.score)

def initLocalCondition(localCondition, condition):
    localCondition['A'] = random.choice(condition)
    localCondition['B'] = random.choice(condition)

def main():
    condition = ['sujo', 'limpo']
    localCondition = {'A': '', 'B': ''}
    initLocalCondition(localCondition, condition)
    print(localCondition)
    agent = VacuumAgent()
    agent.movement(localCondition)
    
main()
