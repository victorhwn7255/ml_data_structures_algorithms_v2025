def singleNumber(nums: list[int]):
  ones = 0
  twos = 0
  for x in nums:
    ones = (ones ^ x) & ~twos
    twos = (twos ^ x) & ~ones
  
  return ones


print(singleNumber([2,2,3,2]))
print(singleNumber([0,1,0,1,0,1,99]))