def permute(nums: list[int]):
  results = []
  def backtrack(path: list, used: set):
    if len(path) == len(nums):
      results.append(path.copy())
      return
    
    for num in nums:
      if num in used:
        continue
      path.append(num)
      used.add(num)
      backtrack(path, used)
      path.pop()
      used.remove(num)
  
  backtrack([], set())
  return results


print(permute([1,2,3]))
print(permute([0,1]))
print(permute([1]))