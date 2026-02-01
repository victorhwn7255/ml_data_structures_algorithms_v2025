def plusOne(digits: list[int]):
  for i in range(len(digits)-1, -1, -1):
    if digits[i] < 9:
      digits[i] += 1
      return digits
    else:
      digits[i]=0
  
  return [1] + digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))