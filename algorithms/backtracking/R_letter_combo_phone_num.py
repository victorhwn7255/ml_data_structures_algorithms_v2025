def letterCombinations(digits: str):
  mapping = {
    '2': "abc", '3': "def", '4': "ghi",
    '5': "jkl", '6': "mno", '7': "pqrs",
    '8': "tuv", '9': "wxyz"
  }
  results = []
  
  def dfs(i, path: list):
    if i == len(digits):
      results.append(''.join(path))
      return
    
    digit = digits[i]
    for char in mapping[digit]:
      path.append(char)
      dfs(i+1, path)
      path.pop()
  
  if len(digits) == 0:
    return []
  
  dfs(0, [])
  
  return results


print(letterCombinations("23"))
print(letterCombinations("2"))