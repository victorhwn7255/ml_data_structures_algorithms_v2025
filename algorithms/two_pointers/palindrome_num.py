def isPalindrome(x: int):
  digits = list(str(x))
  left = 0
  right = len(digits)-1
  
  while left < right:
    if digits[left] != digits[right]:
      return False
    left += 1
    right -= 1
  
  return True


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))