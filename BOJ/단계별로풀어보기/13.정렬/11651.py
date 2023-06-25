#좌표 정렬하기2

import sys
input = sys.stdin.readline

n = int(input())

dots = []
for _ in range(n):
  x, y = map(int, input().split())
  dots.append((x, y))

sorted_dots = sorted(dots, key=lambda x:(x[1], x[0]))
for x in sorted_dots:
  print(x[0], x[1])
