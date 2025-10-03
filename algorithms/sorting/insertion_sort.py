def insertion_sort(my_list: list[int]) -> list:
  for i in range(1, len(my_list)):
    temp = my_list[i]
    j = i - 1
    while temp < my_list[j] and j > -1:
      my_list[j+1] = my_list[j]
      my_list[j] = temp
      j -= 1
  
  return my_list



my_list_1 = [12, 39, 99, 66, 33, 69]

print(insertion_sort(my_list_1))