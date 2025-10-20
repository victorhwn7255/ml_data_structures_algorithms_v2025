def canVisitAllRooms(rooms: list[list[int]]) -> bool:
  visited = set()
  
  def dfs(room:int):
    if room in visited:
      return 
    visited.add(room)
    for key in rooms[room]:
      dfs(key)
  
  dfs(0)
  
  return len(visited) == len(rooms)

rooms_1 = [[1],[2],[3],[]]
rooms_2 = [[1,3],[3,0,1],[2],[0]]

print(canVisitAllRooms(rooms_1))
print(canVisitAllRooms(rooms_2))