def myPow(x: float, n: int):
  result = 1
  
  if n < 0:
    x = 1 / x
    n = -n
    
  while n > 0:
    if n % 2 == 1:
      result *= x
    x *= x
    n //= 2
    
  return result

print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))