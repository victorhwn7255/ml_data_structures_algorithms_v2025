def increasingTriplet(nums: list[int]) -> bool:
  first = 2**31 - 1
  second = 2**31 - 1
  
  for num in nums:
    if num <= first:
      first = num
    elif num <= second:
      second = num
    else:
      return True
  
  return False


nums_1 = [1,2,3,4,5]
nums_2 = [5,4,3,2,1]
nums_3 = [2,1,5,0,4,6]

print(increasingTriplet(nums_1))
print(increasingTriplet(nums_2))
print(increasingTriplet(nums_3))