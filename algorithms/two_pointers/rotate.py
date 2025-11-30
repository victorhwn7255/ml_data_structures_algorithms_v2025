def rotate(nums: list[int], k: int):
  n= len(nums)
  k = k % n
  
  if k == 0:
    return
  
  nums[:0] = [0] * k
  for i in range(k):
    nums[i] = nums[i + n]
  
  nums[len(nums) - k : ] = []
  
  print(nums)
  

nums_1 = [1,2,3,4,5,6,7]
nums_2 = [-1,-100,3,99]

rotate(nums_1, 3)
rotate(nums_2, 2)