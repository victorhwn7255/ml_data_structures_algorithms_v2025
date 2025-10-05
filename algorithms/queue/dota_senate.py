def predictPartyVictory(senate: str) -> str:
  party_r = []
  party_d = []
  
  for i in range(len(senate)):
    if senate[i] == "R":
      party_r.append(i)
    else:
      party_d.append(i)
      
  while party_r and party_d:
    r = party_r.pop(0)
    d = party_d.pop(0)
    
    if r < d:
      party_r.append(r + len(senate))
    else:
      party_d.append(d + len(senate))
  
  return "Radiant" if party_r else "Dire"


senate_1 = "RD"
senate_2 = "RDD"

print(predictPartyVictory(senate_1))
print(predictPartyVictory(senate_2))