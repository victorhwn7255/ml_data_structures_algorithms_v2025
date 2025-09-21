def isSubsequence(s: str, t: str) -> bool:
  i=0
  j=0
  
  while i < len(s) and j < len(t):
    if s[i] == t[j]:
      i += 1
    j += 1
    
  return i == len(s)

s_1 = "abc"
t_1 = "ahbgdc"

s_2 = "axc"
t_2 = "ahbgdc"

print(isSubsequence(s_1, t_1))
print(isSubsequence(s_2, t_1))