def wordPattern(pattern: str, s: str):
  char_to_word = {}
  word_to_char = {}
  words = s.split()
  
  if len(pattern) != len(words):
      return False
  
  for char, word in zip(pattern, words):
    if char in char_to_word and char_to_word[char] != word:
      return False
    if word in word_to_char and word_to_char[word] != char:
      return False
    
    char_to_word[char] = word
    word_to_char[word] = char
  
  return True


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))