#공 넣기

n, m = map(int, input().split(" "))
basket = [0]*n  #n개 길이를 가진 임의의 list 생성

for _ in range(m):  
  i, j, k = map(int, input().split(" "))
  # list의 i번째부터 j번째 값을 k로 변경
  for x in range(i, j+1):
    basket[x-1] = k

for x in basket:
  print(x, end=" ")
