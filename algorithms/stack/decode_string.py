def decodeString(s: str) -> str:
  decode_stack = []
  count = 0
  current_str = ""
  
  for char in s:
    if char.isdigit():
      count = count * 10 + int(char)
    
    elif char == '[':
      decode_stack.append((current_str, count))
      current_str = ''
      count = 0
      
    elif char == "]":
      prev_str, repeat_count = decode_stack.pop()
      current_str = prev_str + current_str * repeat_count
      
    else:
      current_str += char
  
  return current_str



s_1 = "3[a]2[bc]"
s_2 = "3[a2[c]]"
s_3 = "2[abc]3[cd]ef"

print(decodeString(s_1))
print(decodeString(s_2))
print(decodeString(s_3))