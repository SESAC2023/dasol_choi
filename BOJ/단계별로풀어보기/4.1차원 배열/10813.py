#공 바꾸기

n, m = map(int, input().split(" "))
basket = [i+1 for i in range(n)]  #1부터 n까지의 자연수로 구성된 list 생성

for _ in range(m):  
  i, j = map(int, input().split(" "))
  temp = basket[i-1]  #교환을 위한 값을 임시로 저장한 변수
  basket[i-1] = basket[j-1]
  basket[j-1] = temp

for x in basket:
  print(x, end=" ")
