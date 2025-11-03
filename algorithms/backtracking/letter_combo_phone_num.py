def letterCombinations(digits: str) -> list[str]:
  digit_to_letters = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
  }
  results = []
  
  if not digits:
    return []
  
  def backtrack(index, path: list):
    if index == len(digits):
      results.append("".join(path))
      return
    
    for char in digit_to_letters[digits[index]]:
      path.append(char)
      backtrack(index + 1, path)
      path.pop()
  
  backtrack(0, [])
  
  return results

test_input_1 = "23"
test_input_2 = "2"

print(letterCombinations(test_input_1))
print(letterCombinations(test_input_2))