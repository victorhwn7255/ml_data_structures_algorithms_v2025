def mySqrt(x):
  if x == 0:
    return 0
  
  result = 1
  while result*result <= x:
    result +=1
  
  return result - 1

print(mySqrt(4))
print(mySqrt(8))


