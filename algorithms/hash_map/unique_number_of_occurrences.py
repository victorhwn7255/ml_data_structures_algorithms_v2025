def uniqueOccurrences(arr: list[int]) -> bool:
  unique_nums = set(arr)
  occur_table = dict.fromkeys(unique_nums, 0)
  
  for num in arr:
    occur_table[num] += 1
  
  dict_values = set(occur_table.values())
  
  return len(occur_table.values()) == len(dict_values)

arr_1 = [1,2,2,1,1,3]
arr_2 = [1,2]
arr_3 = [-3,0,1,-3,1,1,1,-3,10,0]

print(uniqueOccurrences(arr_1))
print(uniqueOccurrences(arr_2))
print(uniqueOccurrences(arr_3))