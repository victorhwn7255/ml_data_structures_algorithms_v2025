def calculate(s: str):
  result = 0
  sign = +1
  num = 0
  stack = []
  
  for char in s:
    if char.isdigit():
      num = num*10 + int(char)
    if char == "+" or char == "-":
      result = result + sign * num
      num = 0
      if char == "+":
        sign = +1
      else:
        sign = -1
    if char == "(":
      stack.append(result)
      stack.append(sign)
      result = 0
      sign = +1
      num = 0
    if char == ")":
      result = result + sign * num
      num = 0
      prev_sign = stack.pop()
      prev_res = stack.pop()
      result = prev_res + prev_sign * result
    if char == " ":
      continue
    
  result = result + sign * num
   
  return result

print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1+(4+5+2)-3)+(6+8)"))
  