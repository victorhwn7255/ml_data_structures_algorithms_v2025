def minReorder(n: int, connections:list[list[int]]):
  visited = set()
  counts = 0
  
  adjacency_graph = {i: [] for i in range(n)}
  for a, b in connections:
    adjacency_graph[a].append((b, 1))
    adjacency_graph[b].append((a, 0))

  def dfs(city):
    nonlocal counts
    visited.add(city)
    for neighbour, need_reverse in adjacency_graph[city]:
      if neighbour not in visited:
        counts += need_reverse
        dfs(neighbour)
  
  dfs(0)
  
  return counts


test_1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
test_2 = [[1,0],[1,2],[3,2],[3,4]]
test_3 = [[1,0],[2,0]]

print(minReorder(6, test_1))
print(minReorder(5, test_2))
print(minReorder(3, test_3))