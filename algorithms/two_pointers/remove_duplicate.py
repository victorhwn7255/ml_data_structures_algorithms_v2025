def removeDuplicates(nums: list[int]):
  i = 0
  j = 1
  
  while j < len(nums):
    if nums[j] != nums[i]:
      i += 1
      nums[i] = nums[j]
      
    j += 1
  
  return i+1

test_nums_1 = [1,1,2]
test_nums_2 = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(test_nums_1))
print(removeDuplicates(test_nums_2))