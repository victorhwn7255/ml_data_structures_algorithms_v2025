def minWindow(s: str, t: str):
  table = {}
  for char in t:
    table[char] = table.get(char, 0) + 1
  window = {}
  formed = 0
  
  left = 0
  min_len = float("inf")
  min_start = 0
  
  for right in range(len(s)):
    char = s[right]
    window[char] = window.get(char, 0) + 1
    
    if char in table and window[char] == table[char]:
      formed += 1
    
    while formed == len(table):
      if right - left + 1 < min_len:
        min_len = right - left + 1
        min_start = left
      
      left_char = s[left]
      window[left_char] -= 1
      
      if left_char in table and window[left_char] < table[left_char]:
        formed -= 1
        
      left += 1
    
  return "" if min_len == float("inf") else s[min_start:min_start + min_len]


print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))