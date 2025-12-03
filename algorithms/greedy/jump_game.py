def canJump(nums: list[int]):
  i = 0
  max_reach = nums[0]
  
  while i < len(nums)-1:
    i += 1
    if i > max_reach:
      return False
    max_reach = max(max_reach, i + nums[i])

  return True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))