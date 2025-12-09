def canCompleteCircuit(gas: list[int], cost: list[int]):
  if sum(gas) < sum(cost):
    return -1
  
  tank = 0
  start = 0
  for i in range(len(gas)):
    tank += gas[i] - cost[i]
    if tank < 0:
      tank = 0
      start = i + 1
  
  return start

gas_1 = [1,2,3,4,5]
gas_2 = [2, 3, 4]

cost_1 = [3,4,5,1,2]
cost_2 = [3, 4, 3]

print(canCompleteCircuit(gas_1, cost_1))
print(canCompleteCircuit(gas_2, cost_2))