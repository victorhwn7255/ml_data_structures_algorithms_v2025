def factorial(num: int) -> int:
  if num == 1:
    return 1
  
  result = num * factorial(num - 1)
  
  return result


print(factorial(3))
print(factorial(6))
print(factorial(9))