def canFinish(numCourses: int, prerequisites: list[list[int]]):
  graph = { i: [] for i in range(numCourses) }
  for a, b in prerequisites:
    graph[b].append(a)
  
  state = [0] * numCourses
  def dfs(course):
    if state[course] == 1:
      return True
    if state[course] == 2:
      return False
    state[course] = 1
    for neighbor in graph[course]:
      if dfs(neighbor) == True:
        return True
    state[course] = 2
    return False
  
  for course in range(numCourses):
    if dfs(course) == True:
      return False
  
  return True

print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))