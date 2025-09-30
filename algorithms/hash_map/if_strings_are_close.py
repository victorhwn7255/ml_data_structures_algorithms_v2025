def closeStrings(word1: str, word2: str) -> bool:
  set_1 = set(word1)
  set_2 = set(word2)
  
  if len(word1) != len(word2) or set_1 != set_2:
    return False
    
  from collections import Counter
  
  count_1 = Counter(word1)
  count_2 = Counter(word2)
  
  return sorted(count_1.values()) == sorted(count_2.values())

word_1_test_1 = 'abc'
word_2_test_1 = 'bca'

word_1_test_2 = 'a'
word_2_test_2 = 'aa'

word_1_test_3 = 'cabbba'
word_2_test_3 = 'abbccc'

word_1_test_4 = 'abbzzca'
word_2_test_4 = 'babzzcz'

print(closeStrings(word_1_test_1, word_2_test_1))
print(closeStrings(word_1_test_2, word_2_test_2))
print(closeStrings(word_1_test_3, word_2_test_3))
print(closeStrings(word_1_test_4, word_2_test_4))