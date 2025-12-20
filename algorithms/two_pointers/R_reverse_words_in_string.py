def reverseWords(s: str):
  words = s.split()
  results = []
  
  for i in range(len(words)-1, -1, -1):
    results.append(words[i])
  
  return " ".join(results)

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))