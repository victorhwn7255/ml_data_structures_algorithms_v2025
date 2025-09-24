def maxVowels(s: str, k: int) -> int:
  vowels = ['a', 'e', 'i', 'o', 'u']
  current_num = sum(1 for char in s[:k] if char in vowels)
  max_num = current_num

  for i in range(k, len(s)):
    if s[i-k] in vowels:
      current_num -= 1
    if s[i] in vowels:
      current_num += 1
    max_num = max(max_num, current_num)
    
    if max_num == k:
      return k

  return max_num


s_1 = "abciiidef"
s_2 = "aeiou"
s_3 = "leetcode"

k_1 = 3
k_2 = 2
k_3 = 3

print(maxVowels(s_1, k_1))
print(maxVowels(s_2, k_2))
print(maxVowels(s_3, k_3))