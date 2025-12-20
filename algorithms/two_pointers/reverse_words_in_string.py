def reverseWords(s: str) -> str:
  string = ' '.join(s.split())
  words = string.split()
  
  reverse_words = words[::-1]
  
  reverse_s = ' '.join(reverse_words)
  
  return reverse_s

test_s_1 = "the sky is blue"
test_s_2 = "  hello world  "
test_s_3 = "a good   example"

print(reverseWords(test_s_1))
print(reverseWords(test_s_2))
print(reverseWords(test_s_3))