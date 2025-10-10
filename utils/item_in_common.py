def item_in_common(list1, list2):
  hash_table = {}
  
  for item in list_1:
    hash_table[item] = True
  
  for item in list2:
    if hash_table.get(item) == True:
      return True
  
  return False

list_1 = [3, 6, 9]
list_2 = [42, 21, 3]

print(item_in_common(list_1, list_2))