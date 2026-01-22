from collections import defaultdict

def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]):
  node_graph = defaultdict(dict)
  for (a, b), value in zip(equations, values):
    node_graph[a][b] = value
    node_graph[b][a] = 1 / value
  
  def dfs(current, target, product, visited):
    if current == target:
      return product
    
    visited.add(current)
    
    for neighbor in node_graph[current]:
      if neighbor not in visited:
        result = dfs(neighbor, target, product*node_graph[current][neighbor], visited)
        if result != -1:
          return result
    
    return -1
  results = []
  for a, b in queries:
    if a not in node_graph or b not in node_graph:
      results.append(-1)
    else:
      visited = set()
      results.append(dfs(a, b, 1, visited))
  
  return results


test_equations_1 = [["a","b"],["b","c"]]
test_equations_2 = [["a","b"],["b","c"],["bc","cd"]]
test_values_1 = [2.0,3.0]
test_values_2 = [1.5,2.5,5.0]
test_queries_1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
test_queries_2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(calcEquation(test_equations_1, test_values_1, test_queries_1))
print(calcEquation(test_equations_2, test_values_2, test_queries_2))
