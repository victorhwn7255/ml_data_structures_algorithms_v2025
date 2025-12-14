def isAnagram(s: str, t: str):
  table = {}
  
  for char in s:
    table[char] = table.get(char, 0) + 1
    
  for char in t:
    table[char] = table.get(char, 0) - 1
  
  return all(count == 0 for count in table.values())

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("ab", "a"))