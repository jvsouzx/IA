import sys
from collections import deque

class Problem:

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):

        raise NotImplementedError

class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


class VacuumProblem(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def find_position_agent(self, state):
        for i in state:
            if(i == (1,1) or i == (0,1)):
                return state.index(i)

    def actions(self, state):

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'DIAGONAL_LEFT_TOP', 'DIAGONAL_RIGHT_TOP', 'DIAGONAL_LEFT_BOT', 'DIAGONAL_RIGHT_BOT', 'SUCK']
        index_position_agent = self.find_position_agent(state)

        if index_position_agent % 3 == 0:
            possible_actions.remove('LEFT')
            if 'DIAGONAL_LEFT_TOP' in possible_actions:
                possible_actions.remove('DIAGONAL_LEFT_TOP')
            if 'DIAGONAL_LEFT_BOT' in possible_actions:
                possible_actions.remove('DIAGONAL_LEFT_BOT')

        if index_position_agent < 3:
            possible_actions.remove('UP')
            if 'DIAGONAL_LEFT_TOP' in possible_actions:
                possible_actions.remove('DIAGONAL_LEFT_TOP')
            if 'DIAGONAL_RIGHT_TOP' in possible_actions:
                possible_actions.remove('DIAGONAL_RIGHT_TOP')

        if index_position_agent % 3 == 2:
            possible_actions.remove('RIGHT')
            if 'DIAGONAL_RIGHT_TOP' in possible_actions:
                possible_actions.remove('DIAGONAL_RIGHT_TOP')
            if 'DIAGONAL_RIGHT_BOT' in possible_actions:  
                possible_actions.remove('DIAGONAL_RIGHT_BOT')
            
        if index_position_agent > 5:
            possible_actions.remove('DOWN')
            if 'DIAGONAL_LEFT_BOT' in possible_actions:
                possible_actions.remove('DIAGONAL_LEFT_BOT')
            if 'DIAGONAL_RIGHT_BOT' in possible_actions:  
                possible_actions.remove('DIAGONAL_RIGHT_BOT')
            
        if state[index_position_agent][0] == 0:
            possible_actions.remove('SUCK')

        return possible_actions

    def result(self, state, action):
        pos = self.find_position_agent(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1, 'DIAGONAL_LEFT_TOP': -4, 'DIAGONAL_RIGHT_TOP': -2, 'DIAGONAL_LEFT_BOT': 2, 'DIAGONAL_RIGHT_BOT': 4, 'SUCK': 0}
        new_position = pos + delta[action]
        if action != 'SUCK':
            new_state[new_position] =  (new_state[new_position][0], 1)
            new_state[pos] = (new_state[pos][0], 0)
        else:
            new_state[new_position] =  (0, 1)
        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal
    

def is_in(elt, seq):
    return any(x is elt for x in seq)


def depth_limited_search(problem, limit=50):

    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    return recursive_dls(Node(problem.initial), problem, limit)

def iterative_deepening_search(problem):
    
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def breadth_first_graph_search(problem):
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

def depth_first_graph_search(problem):
    
    frontier = [(Node(problem.initial))]
    explored = set()
    while frontier:
    
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None
