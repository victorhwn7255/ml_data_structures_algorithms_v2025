def reverseBits(n: int):
  res = 0
  for _ in range(32):
    res = (res << 1) | (n & 1)
    n >>= 1
  
  return res & 0xFFFFFFFF

print(reverseBits(43261596))
print(reverseBits(2147483644))