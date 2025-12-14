def candy(ratings: list[int]):
  assignment = [1] * len(ratings)
  
  for i in range(len(ratings)-1):
    if ratings[i] < ratings[i+1]:
      assignment[i+1] = assignment[i] + 1
      
  for j in range(len(ratings)-1, 0, -1):
    if ratings[j-1] > ratings[j]:
      assignment[j-1] = max(assignment[j] + 1, assignment[j-1])
  
  return sum(assignment)

print(candy([1,0,2]))
print(candy([1,2,2]))