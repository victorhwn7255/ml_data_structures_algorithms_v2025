def evalRPN(tokens: list[str]):
  stack = []
  result = 0
  
  for item in tokens:
    if item in ["+", "-", "*", "/"]:
      first_num = stack.pop()
      second_num = stack.pop()
      if item == "+":
        result = second_num + first_num
      if item == "-":
        result = second_num - first_num
      if item == "*":
        result = second_num * first_num
      if item == "/":
        result = int(second_num / first_num)
      stack.append(result)
    else:
      stack.append(int(item))
  
  return stack[0]


print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))