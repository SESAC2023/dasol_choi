#알고리즘 수업 - 점근적 표기 1

# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

for n in range(n0, 101):
  fn = a1*n + a0
  gn = n
  if fn > c*gn:
    print(0)
    break
else:
  print(1)
