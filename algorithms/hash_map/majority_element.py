def majorityElement(nums: list[int]):
  table = {}
  for num in nums:
    table[num] = table.get(num, 0) + 1
  
  for key, value in table.items():
    if value > len(nums)/2:
      return key
  


nums_1 = [3,2,3]
nums_2 = [2,2,1,1,1,2,2]

print(majorityElement(nums_1))
print(majorityElement(nums_2))