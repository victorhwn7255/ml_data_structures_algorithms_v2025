def minMutation(startGene: str, endGene: str, bank: list[str]):
  if endGene not in bank:
    return -1
  
  validGenes = set(bank)
  visited = set()
  queue = [(startGene, 0)]
  visited.add(startGene)
  
  while queue:
    gene, steps = queue.pop(0)
    
    if gene == endGene:
      return steps
    
    for i in range(len(gene)):
      for char in ['A', 'C', 'G', 'T']:
        if char == gene[i]:
          continue
        
        mutated = gene[:i] + char + gene[i+1:]
        
        if mutated in validGenes and mutated not in visited:
          visited.add(mutated)
          queue.append((mutated, steps+1))
  
  return -1


print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))