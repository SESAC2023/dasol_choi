#블랙잭

# 카드를 3장 뽑는 모든 경우의 수 구해서 조건 비교
n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(n-2):
  c1 = cards[i]
  for j in range(i+1, n-1):
    c2 = cards[j]
    for k in range(j+1, n):
      c3 = cards[k]
      s = c1 + c2 + c3
      if s >= max_sum and s <= m:
        max_sum = s
print(max_sum)
