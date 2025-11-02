def comboSum(candidates: list[int], target):
  result = []
  
  def backtrack(start, remaining, path: list):
    if remaining == 0:
      result.append(path[:])
      return
    
    if remaining < 0:
      return
    
    for i in range(start, len(candidates)):
      num = candidates[i]
      path.append(num)
      backtrack(i, remaining - num, path)
      path.pop()
      
  backtrack(0, target, [])
  
  return result

test_candidates_1 = [2,3,6,7]
target_1 = 7

print(comboSum(test_candidates_1, target_1))

