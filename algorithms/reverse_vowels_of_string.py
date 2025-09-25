def reverseVowels(s: str) -> str:
  vowels = set('aAeEiIoOuU')
  temp = []
  char_list = []
  
  for char in s:
    char_list.append(char)
    if char in vowels:
      temp.append(char)
  
  for i in range(len(char_list)):
    if char_list[i] in vowels:
      char_list[i] = temp.pop()
      
  return ''.join(char_list)

test_s = "IceCreAm"
test_s_2 = "leetcode"

print(reverseVowels(test_s))
print(reverseVowels(test_s_2))