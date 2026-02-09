def combinationSum(candidates: list[int], target: int):
  candidates.sort()
  results = []
  
  def backtrack(start, remaining, current_combo: list):
    if remaining == 0:
      results.append(current_combo.copy())
      
    for i in range(start, len(candidates)):
      if candidates[i] > remaining:
        break
      current_combo.append(candidates[i])
      backtrack(i, remaining-candidates[i], current_combo)
      current_combo.pop()
  
  backtrack(0, target, [])
  return results


print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))