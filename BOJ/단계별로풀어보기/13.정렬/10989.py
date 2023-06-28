#수 정렬하기 3

import sys
input = sys.stdin.readline

#계수 정렬
n = int(input())

cnt = [0] * 10001

for _ in range(n):
  num = int(input())
  cnt[num ] += 1

for i in range(10001):
  for j in range(cnt[i]):
    print(i)
