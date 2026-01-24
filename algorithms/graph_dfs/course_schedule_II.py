def findOrder(numCourses: int, prerequisites: list[list[int]]):
  graph = { i: [] for i in range(numCourses)}
  for a,b in prerequisites:
    graph[b].append(a)
  states = [0] * numCourses
  results = []
  
  def dfs(course):
    if states[course] == 1:
      return True
    if states[course] == 2:
      return False
    states[course] = 1
    for neighbor in graph[course]:
      if dfs(neighbor):
        return True
    states[course] = 2
    results.append(course)
    return False
  
  for course in range(numCourses):
    if dfs(course):
      return []
  results.reverse()
  return results

print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))


