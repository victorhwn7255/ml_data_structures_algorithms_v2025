def fib(n):
  memo = [0, 1]
  if n < 2:
    return memo[n]
  
  for i in range(2, n+1):
    memo.append(memo[i-1] + memo[i-2])
  
  return memo[n]

n_1 =2
n_2 = 3
n_3 = 4

print(fib(n_1))
print(fib(n_2))
print(fib(n_3))