def eraseOverlapIntervals(intervals: list[list[int]]):
  sorted_list = sorted(intervals, key=lambda x: x[1])
  
  last_end = float('-inf')
  count = 0
  
  for i in range(len(sorted_list)):
    if sorted_list[i][0] >= last_end:
      last_end = sorted_list[i][1]
      count += 1
  
  return len(sorted_list) - count


test_intervals_1 = [[1,2],[2,3],[3,4],[1,3]]
test_intervals_2 = [[1,2],[1,2],[1,2]]
test_intervals_3 = [[1,2],[2,3]]

print(eraseOverlapIntervals(test_intervals_1))
print(eraseOverlapIntervals(test_intervals_2))
print(eraseOverlapIntervals(test_intervals_3))