#좌표 정렬하기

import sys
input = sys.stdin.readline

n = int(input())

dots = []
for _ in range(n):
  x, y = map(int, input().split())
  dots.append((x, y))

for x in sorted(dots):
  print(x[0], x[1])
