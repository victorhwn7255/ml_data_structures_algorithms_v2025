def trailingZeroes(n: int):
  count = 0
  while n >= 5:
    n //= 5
    count += n
  
  return count


print(trailingZeroes(3))
print(trailingZeroes(5))
print(trailingZeroes(0))