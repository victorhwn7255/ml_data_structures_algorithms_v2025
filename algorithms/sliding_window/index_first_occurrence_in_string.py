def strStr(haystack: str, needle: str):
  for i in range(len(haystack) - len(needle) + 1):
    sub_str = haystack[i:i+len(needle)]
    if sub_str == needle:
      return i
  return -1

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))