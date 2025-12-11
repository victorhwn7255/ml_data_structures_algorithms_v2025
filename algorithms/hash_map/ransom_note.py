def canConstruct(ransomNote: str, magazine: str):
  table = {}
  for char in magazine:
    table[char] = table.get(char, 0) + 1
      
  for char in ransomNote:
    if table.get(char, 0) == 0:
      return False
    table[char] -= 1
      
  return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))