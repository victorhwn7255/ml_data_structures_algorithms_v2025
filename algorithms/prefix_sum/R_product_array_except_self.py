def productExceptSelf(nums: list[int]):
  n = len(nums)
  answer = [1] * n
  
  for i in range(1, n):
    answer[i] = nums[i-1] * answer[i-1]
  
  suffix = 1
  j = n - 1
  while j >= 0:
    answer[j] = answer[j] * suffix
    suffix *= nums[j]
    j -= 1
  
  return answer


print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))