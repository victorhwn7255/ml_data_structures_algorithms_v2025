def asteroidCollision(asteroids: list[int]) -> list[int]:
  remain_stack = []
  
  for item in asteroids:
    while remain_stack and remain_stack[-1] > 0 and item < 0:
      if abs(remain_stack[-1]) < abs(item):
        remain_stack.pop()
      elif abs(remain_stack[-1]) == abs(item):
        remain_stack.pop()
        break
      else:
        break
      
    else:
      remain_stack.append(item)
  
  return remain_stack



asteroids_1 = [5,10,-5]
asteroids_2 = [8,-8]
asteroids_3 = [10,2,-5]

print(asteroidCollision(asteroids_1))
print(asteroidCollision(asteroids_2))
print(asteroidCollision(asteroids_3))