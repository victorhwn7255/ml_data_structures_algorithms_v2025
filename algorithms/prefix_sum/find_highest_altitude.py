def largestAltitude(gain: list[int]) -> int:
  points = []
  points.append(0)
  
  for i in range(len(gain)):
    points.append(gain[i] + points[i])
  
  return max(points)

gain_1 = [-5,1,5,0,-7]
gain_2 = [-4,-3,-2,-1,4,3,2]

print(largestAltitude(gain_1))
print(largestAltitude(gain_2))