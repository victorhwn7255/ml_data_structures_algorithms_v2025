def longestCommonPrefix(strs: list[str]):
  sorted_strs = sorted(strs)
  first = sorted_strs[0]
  last = sorted_strs[-1]

  i = 0
  while i < len(first) and first[i] == last[i]:
    i += 1
    
  return first[:i]

strs_1 = ["flower","flow","flight"]
strs_2 = ["dog","racecar","car"]

print(longestCommonPrefix(strs_1))
print(longestCommonPrefix(strs_2))