def simplifyPath(path: str):
  parts = path.split("/")
  stack = []
  
  for item in parts:
    if item == "" or item == ".":
      continue
    elif item == "..":
      if len(stack) != 0:
        stack.pop()
    else:
      stack.append(item)
  
  return "/" + "/".join(stack)


print(simplifyPath("/home/"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/../"))
print(simplifyPath("/.../a/../b/c/../d/./"))