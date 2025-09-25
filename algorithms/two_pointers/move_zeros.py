def moveZeroes(nums: list[int]) -> None:
  i = 0
  
  for j in range(len(nums)):
    if nums[j] !=0:
      nums[i] = nums[j]
      i += 1
      
  while i < len(nums):
    nums[i] = 0
    i += 1
  
  return nums


nums_1 = [0,1,0,3,12]
nums_2 = [0]

print(moveZeroes(nums_1))