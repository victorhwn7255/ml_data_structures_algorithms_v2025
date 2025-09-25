def maxArea(height: list[int]) -> int:
  max_area = 0
  left = 0
  right = len(height) - 1
  
  while left < right:
    current_area = min(height[left], height[right]) * (right - left)
    max_area = max(current_area, max_area)
    
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1
  
  return max_area


height_test = [1,8,6,2,5,4,8,3,7]
print(maxArea(height_test))