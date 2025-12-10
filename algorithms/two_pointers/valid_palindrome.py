def isPalindrome(s: str):
  combined_s = "".join(ch for ch in s if ch.isalnum()).lower()
  
  left = 0
  right = len(combined_s) - 1
  
  while right >= left:
    if combined_s[right] == combined_s[left]:
      right -= 1
      left += 1
    else:
      return False
    
  return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))