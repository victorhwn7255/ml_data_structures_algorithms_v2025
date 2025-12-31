def findMinArrowShots(points: list[list[int]]):
  points.sort(key = lambda x : x[0])
  arrows = 1
  current_end = points[0][1]
  
  for i in range(1, len(points), 1):
    if points[i][0] > current_end:
      arrows += 1
      current_end = points[i][1]
    else:
      current_end = min(current_end, points[i][1])
  
  return arrows

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))