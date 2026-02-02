def singleNumber(nums: list[int]):
  x = 0
  for v in nums:
    x ^= v
  
  return x


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))