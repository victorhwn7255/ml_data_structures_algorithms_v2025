def isValid(s: str):
  stack_list = []
  parentheses_table = {
    "(" : ")",
    "{" : "}",
    "[" : "]"
  }
  
  for char in s:
    if stack_list and stack_list[-1] in parentheses_table and char == parentheses_table[stack_list[-1]]:
      stack_list.pop()
    else:
      stack_list.append(char)
  
  return len(stack_list) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))
