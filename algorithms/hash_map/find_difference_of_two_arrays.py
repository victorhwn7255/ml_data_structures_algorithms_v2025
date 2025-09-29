def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
  set_1 = set(nums1)
  set_2 = set(nums2)
  
  unique_1 = list(set_1 - set_2)
  unique_2 = list(set_2 - set_1)
  
  return [unique_1, unique_2]


nums_1_test_1 = [1,2,3]
nums_2_test_1 = [2,4,6]

nums_1_test_2 = [1,2,3,3]
nums_2_test_2 = [1,1,2,2]

print(findDifference(nums_1_test_1, nums_2_test_1))
print(findDifference(nums_1_test_2, nums_2_test_2))