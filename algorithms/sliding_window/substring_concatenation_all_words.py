from collections import Counter

def findSubstring(s: str, words: list[str]):
  word_size = len(words[0])
  window_size = word_size * len(words)
  word_map = Counter(words)
  result = []
  
  if window_size > len(s):
    return []
  
  for offset in range(word_size):
    left = offset
    seen = Counter()
    count = 0
    
    for right in range(offset, len(s) - word_size + 1, word_size):
      word = s[right : right + word_size]
      if word in word_map:
        seen[word] += 1
        count += 1
        
        while seen[word] > word_map[word]:
          left_word = s[left : left + word_size]
          seen[left_word] -= 1
          left += word_size
          count -= 1
        
        if count == len(words):
          result.append(left)
          
      else:
        seen.clear()
        count = 0
        left = right + word_size
  
  return result


print(findSubstring("barfoothefoobarman", ["foo","bar"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))