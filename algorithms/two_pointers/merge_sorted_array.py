def merge(nums1: list[int], m: int, nums2: list[int], n: int):
  i = m - 1
  j = n - 1
  k = m + n - 1
  
  while j >= 0:
    if i >=0 and nums1[i] > nums2[j]:
      nums1[k] = nums1[i]
      i -= 1
    else:
      nums1[k] = nums2[j]
      j -= 1
    k -= 1
  
  print(nums1)
  
test_nums1 = [1,2,3,0,0,0]
test_nums2 = [2,5,6]

print(merge(test_nums1, 3, test_nums2, 3))