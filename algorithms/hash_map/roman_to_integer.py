def romanToInt(s: str):
  SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
  
  result = 0
  
  for i in range(len(s)):
    if i + 1 < len(s) and SYMBOLS[s[i]] < SYMBOLS[s[i+1]]:
      result -= SYMBOLS[s[i]]
    else:
      result += SYMBOLS[s[i]]
        
  return result

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))