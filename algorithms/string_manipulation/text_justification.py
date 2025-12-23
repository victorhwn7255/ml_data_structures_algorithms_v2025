def fullJustify(words: list[str], maxWidth: int):
  result = []
  i = 0
  
  while i < len(words):
    line_words = []
    line_length = 0
    
    while i<len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
      line_words.append(words[i])
      line_length += len(words[i])
      i += 1
      
    if i == len(words):
      line = " ".join(line_words)
      line += " " * (maxWidth - len(line))
      
    elif len(line_words) == 1:
      line = line_words[0]
      line += " " * (maxWidth - len(line))
      
    else:
      total_spaces = maxWidth - line_length
      gaps = len(line_words) - 1
      
      space_each = total_spaces // gaps
      extra_spaces = total_spaces % gaps
      
      line = ""
      for j in range(len(line_words)):
        line += line_words[j]
        if j < gaps:
          line += " " * space_each
          if extra_spaces > 0:
            line += " "
            extra_spaces -= 1
  
    result.append(line)
    
  return result


words_test_1 = ["This", "is", "an", "example", "of", "text", "justification."]
words_test_2 = ["What","must","be","acknowledgment","shall","be"]
words_test_3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]

print(fullJustify(words_test_1, 16))
print(fullJustify(words_test_2, 16))
print(fullJustify(words_test_3, 20))