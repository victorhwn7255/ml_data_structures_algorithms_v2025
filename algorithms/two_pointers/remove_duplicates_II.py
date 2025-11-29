def removeDuplicates(nums: list[int]):
  if len(nums) <= 2:
    return len(nums)
  
  slow = 1
  fast = 1
  count = 1
  
  while fast < len(nums):
    if nums[fast] == nums[fast - 1]:
      count += 1
    else:
      count = 1
    
    if count <= 2:
      slow += 1
      nums[slow - 1] = nums[fast]
      
    fast += 1
    
  print(nums)
  return slow
  

test_nums_1 = [1,1,1,2,2,3]
test_nums_2 = [0,0,1,1,1,1,2,3,3]

print(removeDuplicates(test_nums_1))
print(removeDuplicates(test_nums_2))