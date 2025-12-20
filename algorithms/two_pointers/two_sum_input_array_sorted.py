def twoSum(numbers: list[int], target: int):
  left = 0
  right = len(numbers)-1
  
  while left < right:
    if numbers[left] + numbers[right] < target:
      left += 1
    elif numbers[left] + numbers[right] > target:
      right -= 1
    else:
      return [left+1, right+1]
    

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1, 0], -1))