def hIndex(citations: list[int]):
  sorted_citations = sorted(citations, reverse=True)
  
  for i in range(len(citations)):
    if sorted_citations[i] == i + 1:
      return i + 1
    elif sorted_citations[i] < i + 1:
      return i

  return len(citations)

citations_1 = [3,0,6,1,5]
citations_2 = [1,3,1]

print(hIndex(citations_1))
print(hIndex(citations_2))