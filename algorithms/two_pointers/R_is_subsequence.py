def isSubsequence(s: str, t: str):
  i = 0
  j = 0
  
  while i < len(s):
    if j >= len(t):
      return False
    
    if s[i] == t[j]:
      i += 1
    j += 1
  
  return True

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))