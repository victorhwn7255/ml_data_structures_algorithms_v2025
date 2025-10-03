def selection_sort(my_list: list[int]):
  for i in range(len(my_list)-1):
    min_index = i
    for j in range(i+1, len(my_list)):
      if my_list[j] < my_list[min_index]:
        min_index = j
    
    if i != min_index:
      temp = my_list[i]
      my_list[i] = my_list[min_index]
      my_list[min_index] = temp
    
  return my_list


my_list_1 = [12, 39, 99, 66, 33, 69]

print(selection_sort(my_list_1))