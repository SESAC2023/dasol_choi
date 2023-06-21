#약수 구하기
# N의 약수들 중 K번째로 작은 수를 출력
# N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력

n, k = map(int, input().split(" "))

factors = []

for i in range(1, n+1):
  if n % i == 0:
    factors.append(i)

if len(factors) < k:
  print(0)
else:
  print(factors[k-1])
