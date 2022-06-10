import problem

# st0 = [{'M': 3, 'C': 3, 'B': 1}, {'M': 0, 'C': 0, 'B': 0}]
# st1 = [{'M': 2, 'C': 2, 'B': 0}, {'M': 1, 'C': 1, 'B': 1}]  
# st2 =[{'M': 3, 'C': 1, 'B': 0}, {'M': 0, 'C': 2, 'B': 1}]
# st3 =[{'M': 3, 'C': 2, 'B': 0}, {'M': 0, 'C': 1, 'B': 1}]
# st4 =[{'M': 3, 'C': 2, 'B': 1}, {'M': 0, 'C': 1, 'B': 0}]  
# st5 =[{'M': 3, 'C': 0, 'B': 0}, {'M': 0, 'C': 3, 'B': 1}]  
# st6 =[{'M': 3, 'C': 1, 'B': 1}, {'M': 0, 'C': 2, 'B': 0}]  
# st7 =[{'M': 1, 'C': 1, 'B': 0}, {'M': 2, 'C': 2, 'B': 1}]  
# st8 =[{'M': 2, 'C': 2, 'B': 1}, {'M': 1, 'C': 1, 'B': 0}]
# st9 =[{'M': 0, 'C': 2, 'B': 0}, {'M': 3, 'C': 1, 'B': 1}]  
# st10 =[{'M': 0, 'C': 3, 'B': 1}, {'M': 3, 'C': 0, 'B': 0}]
# st11 =[{'M': 0, 'C': 1, 'B': 0}, {'M': 3, 'C': 2, 'B': 1}]  
# st12 =[{'M': 0, 'C': 2, 'B': 1}, {'M': 3, 'C': 1, 'B': 0}]  
# st13 =[{'M': 1, 'C': 1, 'B': 1}, {'M': 2, 'C': 2, 'B': 0}]  
# st14 =[{'M': 0, 'C': 0, 'B': 0}, {'M': 3, 'C': 3, 'B': 1}] 


graph = problem.UndirectedGraph(dict(
    st0=dict(st1=1, st2=1, st3=1),
    st1=dict(st4=1),
    st4=dict(st5=1),
    st5=dict(st6=1),
    st6=dict(st7=1),
    st7=dict(st8=1),
    st8=dict(st9=1),
    st9=dict(st10=1),
    st10=dict(st11=1),
    st11=dict(st12=1, st13=1),
    st12=dict(st14=1),
))

cmp = problem.GraphProblem('st0', 'st14', graph)
print(problem.depth_first_graph_search(cmp).solution())