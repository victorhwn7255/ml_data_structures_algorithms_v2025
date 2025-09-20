def productExceptSelf(nums: list[int]) -> list[int]:
  n = len(nums)
  answers = [1] * n
  
  for i in range (1, n):
    answers[i] = answers[i-1] * nums[i-1]
    
  print("prefix: ", answers) 
  
  suffix = 1
  for i in range(n-1, -1, -1):
    answers[i] = answers[i] * suffix
    suffix *= nums[i]
  
  return answers

nums_1 = [1,2,3,4]
nums_2 = [-1,1,0,-3,3]

print(productExceptSelf(nums_1))
print(productExceptSelf(nums_2))