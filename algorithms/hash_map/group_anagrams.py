def groupAnagrams(strs: list[str]):
  if len(strs) == 0:
    return [[""]]
  
  table = {}
  
  for word in strs:
    key = "".join(sorted(word))
    if key not in table:
      table[key] = []
    table[key].append(word)
    
  return list(table.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["a"]))
print(groupAnagrams([""]))