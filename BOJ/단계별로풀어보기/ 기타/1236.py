# 성 지키기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

castle = [list(input().strip()) for _ in range(n)]

x, y = set(), set()
for i in range(len(castle)):
  for j in range(len(castle[i])):
    if castle[i][j] == 'X':
      x.add(i)
      y.add(j)

print(max(m-len(y), n-len(x)))
