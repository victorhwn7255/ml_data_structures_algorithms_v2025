def hIndex(citations: list[int]):
  sorted_citations = sorted(citations, reverse=True)
  
  for i in range(len(citations)):
    if sorted_citations[i] == i + 1:
      return i + 1
    elif sorted_citations[i] < i + 1:
      return i

  return len(citations)

doctor_paulinka = [6, 1, 3, 0, 4, 5, 7, 9, 11]
#citations_2 = [1,3,1]

print("the H-Index of Dr Paulinka is: ", hIndex(doctor_paulinka))
#print(hIndex(citations_2))