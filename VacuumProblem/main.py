import problem
import agents
import random
import time
initial = ((1, 0), (1, 0), (1, 0),
           (0, 0), (0, 1), (0, 0),
           (0, 0), (0, 0), (0, 0))

goal = ((0, 0), (0, 0), (0, 0),
        (0, 0), (0, 1), (0, 0),
        (0, 0), (0, 0), (0, 0))

#Preenchimento aleatório com base na probabilidade de 20%
initial_random = ()
listInitialRandom = []

for i in range(len(initial)):
        if(random.choice([0,1,2,3,4]) == 0):
                listInitialRandom.append((1,0))
        else:
                listInitialRandom.append((0,0))

listInitialRandom[4] = (listInitialRandom[4][0], 1)
initial_random = tuple(listInitialRandom)

print("Estado Inicial: "+ str(initial_random))

print("\n")

#Execução da busca do caminho
vp = problem.VacuumProblem(initial_random, goal)
t1 = time.perf_counter()
solutionBPI = problem.iterative_deepening_search(vp).solution()
t2 = time.perf_counter()
print("Busca em Profundidade Iterativa :")
print(solutionBPI)
print(f"Tempo de Busca: {t2-t1:.4f} segundos")

print("\n")

#Agente reativo randômico
ra = agents.RandomReflexAgent(initial_random)
ra.randomMovement(goal)
print("Pontuação Agente Reativo Aleatório: " + str(len(ra.movements)))
print(ra.movements)

print("\n")

#Execução da busca pelo agente
sa = agents.SearchAgent(solutionBPI, initial_random)
sa.movement()
print("Pontuação Agente de Busca: " + str(len(solutionBPI)+(t2 - t1)))
print(solutionBPI)
