def trap(height: list[int]):
  left = 0
  right = len(height)-1
  leftMax = 0
  rightMax = 0
  water = 0
  
  while left < right:
    if height[left] <= height[right]:
      leftMax = max(leftMax, height[left])
      water += leftMax - height[left]
      left += 1
    else:
      rightMax = max(height[right], rightMax)
      water += rightMax - height[right]
      right -= 1
  
  return water


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))