def rob(nums: list[int]):
  if len(nums) == 1:
    return nums[0]
  
  prev_0 = nums[0]
  prev_1 = max(nums[0], nums[1])
  
  for i in range(2, len(nums)):
    current = max(prev_1, prev_0 + nums[i])
    prev_0 = prev_1
    prev_1 = current

  return prev_1


nums_1 = [ 1, 2, 3, 1 ]
nums_2 = [ 2, 7, 9, 3, 1 ]

print(rob(nums_1))
print(rob(nums_2))