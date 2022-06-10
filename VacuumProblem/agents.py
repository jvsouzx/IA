import random

class RandomReflexAgent():
    def __init__(self, environment):
        self.environment = environment
        self.movements = []

    def find_position_agent(self, environment):
        for i in environment:
            if(i == (1, 1) or i == (0, 1)):
                return environment.index(i)

    def possibleActions(self):

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'DIAGONAL_LEFT_TOP', 'DIAGONAL_RIGHT_TOP', 'DIAGONAL_LEFT_BOT', 'DIAGONAL_RIGHT_BOT']
        agent_pos = self.find_position_agent(self.environment)
        
        if agent_pos % 3 == 0:
            possible_actions.remove('LEFT')
            if 'DIAGONAL_LEFT_TOP' in possible_actions:
               possible_actions.remove('DIAGONAL_LEFT_TOP')
            if 'DIAGONAL_LEFT_BOT' in possible_actions:
               possible_actions.remove('DIAGONAL_LEFT_BOT')

        if agent_pos < 3:
            possible_actions.remove('UP')
            if 'DIAGONAL_LEFT_TOP' in possible_actions:
               possible_actions.remove('DIAGONAL_LEFT_TOP')
            if 'DIAGONAL_RIGHT_TOP' in possible_actions:
               possible_actions.remove('DIAGONAL_RIGHT_TOP')

        if agent_pos % 3 == 2:
            possible_actions.remove('RIGHT')
            if 'DIAGONAL_RIGHT_TOP' in possible_actions:
               possible_actions.remove('DIAGONAL_RIGHT_TOP')
            if 'DIAGONAL_RIGHT_BOT' in possible_actions:
               possible_actions.remove('DIAGONAL_RIGHT_BOT')

        if agent_pos > 5:
            possible_actions.remove('DOWN')
            if 'DIAGONAL_LEFT_BOT' in possible_actions:
               possible_actions.remove('DIAGONAL_LEFT_BOT')
            if 'DIAGONAL_RIGHT_BOT' in possible_actions:
               possible_actions.remove('DIAGONAL_RIGHT_BOT')

        return possible_actions

    def randomMovement(self, goal):
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1, 'DIAGONAL_LEFT_TOP': -4,
                 'DIAGONAL_RIGHT_TOP': -2, 'DIAGONAL_LEFT_BOT': 2, 'DIAGONAL_RIGHT_BOT': 4, 'SUCK': 0}
        new_states = list(self.environment)
        while self.environment != goal:
            action = random.choice(self.possibleActions())
            pos = self.find_position_agent(self.environment)
            new_position = pos + delta[action]
            if new_states[pos][0] == 1:
                self.movements.append('SUCK')
                new_states[pos] = (0, 1)
                self.environment = tuple(new_states)
                new_states = list(self.environment)
            if self.environment == goal:
                break
            self.movements.append(action)
            new_states[new_position] = (new_states[new_position][0], 1)
            new_states[pos] = (new_states[pos][0], 0)
            self.environment = tuple(new_states)

class SearchAgent():
    
    def __init__(self, sequence, environment):
        self.sequence = sequence
        self.environment = environment

    def find_position_agent(self, environment):
        for i in environment:
            if(i == (1, 1) or i == (0, 1)):
                return environment.index(i)

    def movement(self):
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1, 'DIAGONAL_LEFT_TOP': -4,
                 'DIAGONAL_RIGHT_TOP': -2, 'DIAGONAL_LEFT_BOT': 2, 'DIAGONAL_RIGHT_BOT': 4, 'SUCK': 0}
        new_states = list(self.environment)
        for action in self.sequence:
            pos = self.find_position_agent(self.environment)
            new_position = pos + delta[action]
            if action == 'SUCK':
                new_states[pos] = (0, 1)
            else:
                new_states[new_position] = (new_states[new_position][0], 1)
                new_states[pos] = (new_states[pos][0], 0)
            self.environment = tuple(new_states)
       