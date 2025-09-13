def mergeAlternately(word1, word2):
  res = []
  i = 0
  while i < len(word1) and i < len(word2):
    res.append(word1[i])
    res.append(word2[i])
    i += 1
  
  if len(word1) > len(word2):
    res.append(word1[i:])
  else:
    res.append(word2[i:])
  
  return "".join(res)

def doublePointer(word1, word2):
  n1, n2 = len(word1), len(word2)
  res = []
  i = j = 0
  
  while i < n1 or j < n2:
    if i < n1:
      res.append(word1[i])
      i += 1
    if j < n2:
      res.append(word2[j])
      j += 1
      
  return "".join(res)

def test(word):
  res = list(word)
  return res

word_test_1 = 'abcd'
word_test_2 = 'pq'

result = doublePointer(word_test_1, word_test_2)
test_result = test(word_test_1)

print(result)