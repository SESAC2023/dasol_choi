#수 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())
li = sorted([int(input()) for _ in range(n)])

for x in li:
  print(x)

