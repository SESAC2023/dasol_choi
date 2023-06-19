#바구니 뒤집기

n, m = map(int, input().split(" "))
basket = list(range(1, n+1))

for _ in range(m):
  i, j = map(int, input().split(" "))
  while i < j:
    temp = basket[i-1] 
    basket[i-1] = basket[j-1] 
    basket[j-1] = temp
    i += 1
    j -= 1

for num in basket:
  print(num, end=" ")
