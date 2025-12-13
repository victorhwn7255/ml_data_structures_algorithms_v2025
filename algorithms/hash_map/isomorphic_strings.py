def isIsomorphic(s: str, t: str):
  s_to_t = {}
  t_to_s = {}
  
  for char1, char2 in zip(s, t):
    if char1 in s_to_t and s_to_t[char1] != char2:
      return False
    if char2 in t_to_s and t_to_s[char2] != char1:
      return False
    
    s_to_t[char1] = char2
    t_to_s[char2] = char1
    
  return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))