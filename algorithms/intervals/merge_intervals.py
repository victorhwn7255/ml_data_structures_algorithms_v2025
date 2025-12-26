def merge(intervals: list[list[int]]):
  result = []
  intervals.sort(key=lambda x: x[0])
  current_start, current_end = intervals[0]
  
  for start, end in intervals[1:]:
    if start <= current_end:
      current_end = max(current_end, end)
    else:
      result.append([current_start, current_end])
      current_start, current_end = start, end
      
  result.append([current_start, current_end])
      
  return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[4,7],[1,4]]))