# x // 10: remove the last digit
# x % 10: get the last digit

def isPalindrome(x: int):
  if x < 0 or (x % 10 == 0 and x != 0):
    return False
  
  reversed_half = 0
  while x > reversed_half:
    reversed_half = reversed_half * 10 + x % 10
    x //= 10
  
  return x == reversed_half or x == reversed_half // 10


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))