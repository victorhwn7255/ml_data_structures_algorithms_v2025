def bubble_sort(my_list: list[int]) -> list:
  for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
      if my_list[j] > my_list[j+1]:
        temp = my_list[j]
        my_list[j] = my_list[j+1]
        my_list[j+1] = temp
  
  return my_list



my_list_1 = [12, 39, 99, 66, 33, 69]

print(bubble_sort(my_list_1))