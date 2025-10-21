def findCircleNum(isConnected: list[list[int]]):
  n = len(isConnected)
  visited = set()
  
  def dfs(city):
    if city in visited:
      return
    visited.add(city)
    for neighbor in range(n):
      if isConnected[city][neighbor] == 1:
        dfs(neighbor)
        
  province_num = 0
  
  for i in range(n):
    if i not in visited:
      province_num += 1
      dfs(i)
  
  return province_num


test_1 = [[1,1,0],[1,1,0],[0,0,1]]
test_2 = [[1,0,0],[0,1,0],[0,0,1]]

print(findCircleNum(test_1))
print(findCircleNum(test_2))