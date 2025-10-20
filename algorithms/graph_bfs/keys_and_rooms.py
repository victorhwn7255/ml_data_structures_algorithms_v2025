def canVisitAllRooms(rooms: list[list[int]]) -> bool:
  visited = {0}
  queue = [0]
  
  while len(queue) > 0:
    keys = rooms[queue.pop(0)]
    for key in keys:
      if key not in visited:
        visited.add(key)
        queue.append(key)
  
  return len(visited) == len(rooms)

rooms_1 = [[1],[2],[3],[]]
rooms_2 = [[1,3],[3,0,1],[2],[0]]

print(canVisitAllRooms(rooms_1))
print(canVisitAllRooms(rooms_2))