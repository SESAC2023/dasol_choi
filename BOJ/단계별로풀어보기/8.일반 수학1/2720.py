#세탁소 사장 동혁

t = int(input())
coins = [25, 10, 5, 1]  #동전의 종류

for _ in range(t):
  c = int(input())
  for coin in coins:  #가장 큰 단위의 동전부터 순서대로 개수 확인
    print(c//coin, end=" ")
    c = c%coin
