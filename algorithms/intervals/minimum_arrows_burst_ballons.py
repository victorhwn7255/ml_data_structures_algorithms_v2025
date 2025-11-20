def findMinArrowShots(points: list[list[int]]):
  points.sort(key=lambda x: x[1])
  
  arrows = 1
  current_arrow = points[0][1]
  
  for start, end in points:
    if start > current_arrow:
      arrows += 1
      current_arrow = end
  
  return arrows

test_points_1 = [[10,16],[2,8],[1,6],[7,12]]
test_points_2 = [[1,2],[3,4],[5,6],[7,8]]
test_points_3 = [[1,2],[2,3],[3,4],[4,5]]

print(findMinArrowShots(test_points_1))
print(findMinArrowShots(test_points_2))
print(findMinArrowShots(test_points_3))