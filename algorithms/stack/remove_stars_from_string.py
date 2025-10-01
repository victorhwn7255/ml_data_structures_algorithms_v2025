def removeStars(s: str) -> str:
  stack = []
  
  for char in s:
    if char == "*":
      if stack:
        stack.pop()
    else:
      stack.append(char)
  
  return "".join(stack)


s_1 = "leet**cod*e"
s_2 = "erase*****"

print(removeStars(s_1))
print(removeStars(s_2))