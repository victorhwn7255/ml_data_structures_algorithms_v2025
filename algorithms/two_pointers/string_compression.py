def compress(chars: list[str]) -> int:
  write = 0
  read = 0
  
  while read < len(chars):
    target_char = chars[read]
    count = 0
    
    while read < len(chars) and chars[read] == target_char:
      read += 1
      count += 1
    
    chars[write] = target_char
    write += 1
    
    if count > 1:
      for digit in str(count):
        chars[write] = digit
        write += 1
  
  return write

chars_1 = ["a","a","b","b","c","c","c"]
chars_2 = ["a"]
chars_3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(compress(chars_1))
print(compress(chars_2))
print(compress(chars_3))