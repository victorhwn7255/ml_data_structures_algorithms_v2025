def gcdOfStrings(str1, str2):
  def gcd(a, b):
    while b != 0:
      a, b = b, a % b
    return a
  
  if str1 + str2 != str2 + str1:
    return ""
  else:
    g = gcd(len(str1), len(str2))
    return str1[:g]
    
  

str_1 = "ABCABCABC"
str_2 = "ABC"

print(gcdOfStrings(str_1, str_2))