
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]):
  node_graph = {}
  for (a, b), value in zip(equations, values):
    node_graph.setdefault(a, {})[b] = value
    node_graph.setdefault(b, {})[a] = 1/ value
  
  def dfs(current, target, product, visited):
    if current == target:
      return product
    
    visited.add(current)
    for neighbour, val in node_graph[current].items():
      if neighbour not in visited:
        result = dfs(neighbour, target, product*val, visited)
        if result != -1:
          return result
    return -1
  
  results = []
  for a, b in queries:
    if a not in node_graph or b not in node_graph:
      results.append(-1.0)
    else:
      results.append(dfs(a, b, 1, set()))
  
  return results


equations_1 = [["a","b"],["b","c"]]
values_1 = [2.0,3.0]
queries_1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

equations_2 = [["a","b"],["b","c"],["bc","cd"]]
values_2 = [1.5,2.5,5.0]
queries_2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

equations_3 = [["a","b"]]
values_3 = [0.5]
queries_3 = [["a","b"],["b","a"],["a","c"],["x","y"]]

print(calcEquation(equations_1, values_1, queries_1))
print(calcEquation(equations_2, values_2, queries_2))
print(calcEquation(equations_3, values_3, queries_3))