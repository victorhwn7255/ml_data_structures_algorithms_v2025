def combinationSum3(k, n):
  results = []
  
  def backtrack(count, remaining, path:list, start):
    if count == 0 and remaining == 0:
      results.append(path[:])
      return
    
    for num in range(start, 10):
      if remaining >= num:
        path.append(num)
        backtrack(count - 1, remaining - num, path, num + 1)
        path.pop()
      
  backtrack(k, n, [], 1)
  
  return results

k_1 = 3
n_1 = 7

k_2 = 3
n_2 = 9

print(combinationSum3(k_1, n_1))
print(combinationSum3(k_2, n_2))