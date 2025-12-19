def isHappy(n: int):
  seen = set()
  def sum_of_digits(n: int):
    return sum(int(d)**2 for d in str(n))
  
  total = sum_of_digits(n)
  while total != 1:
    if total in seen:
      return False
    seen.add(total)
    total = sum_of_digits(total)
  
  return True

print(isHappy(19))
print(isHappy(2))