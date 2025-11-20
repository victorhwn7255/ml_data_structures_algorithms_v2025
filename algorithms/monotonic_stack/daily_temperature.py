def dailyTemperatures(temperatures: list[int]):
  stack = []
  results = [0] * len(temperatures) 
  
  for i, temp in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < temp:
      prev_i = stack.pop()
      results[prev_i] = i - prev_i
      
    stack.append(i)
  
  return results

test_temp_1 = [73,74,75,71,69,72,76,73]
test_temp_2 = [30,40,50,60]
test_temp_3 = [30,60,90]

print(dailyTemperatures(test_temp_1))
print(dailyTemperatures(test_temp_2))
print(dailyTemperatures(test_temp_3))