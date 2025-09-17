def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
  length = len(flowerbed)
  k = 0
  
  for i in range(length):
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
      flowerbed[i] = 1
      k += 1
      
  return k

flowerbed_1 = [1,0,0,0,1]
n_1 = 2

flowerbed_2 = [1,0,0,0,0,0,0]
n_2 = 2

print(canPlaceFlowers(flowerbed_1, n_1))
print(canPlaceFlowers(flowerbed_2, n_2))