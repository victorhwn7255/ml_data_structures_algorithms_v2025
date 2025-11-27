def removeElement(nums: list[int], val: int):
  i = 0
  j = len(nums) - 1
  
  while i < j:
    if nums[i] == val:
      if nums[j] == val:
        j -= 1
      else:
        nums[i] = nums[j]
        nums[j] = val
    else:
      i += 1
  
  if i == j and nums[i] == val:
    return i
  else:
    return i + 1

test_nums_1 = [3,2,2,3]
test_nums_2 = [0,1,2,2,3,0,4,2]

print(removeElement(test_nums_1, 3))
print(removeElement(test_nums_2, 2))