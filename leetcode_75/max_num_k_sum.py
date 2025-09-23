def maxOperations(nums: list[int], k: int) -> int:
  sort_nums = sorted(nums)

  i = 0
  j = len(sort_nums) - 1
  count = 0
  
  while i < j:
    if sort_nums[i] + sort_nums[j] > k:
      j -= 1
    elif sort_nums[i] + sort_nums[j] < k:
      i += 1
    else:
      count += 1
      i += 1
      j -= 1
  
  return count

nums_1 = [1,2,3,4]
nums_2 = [3,1,3,4,3]
k_1 = 5
k_2 = 6

print(maxOperations(nums_1, k_1))
print(maxOperations(nums_2, k_2))