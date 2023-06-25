#수 정렬하기 3

# 메모리 초과 실패!!!!!!!!!!!!

import sys
input = sys.stdin.readline

#계수 정렬
n = int(input())
li = sorted([int(input()) for _ in range(n)])

cnt = [0] * (n+1)

for i in range(n):
  cnt[li[i]] += 1

for i in range(len(cnt)):
  for j in range(cnt[i]):
    print(i)
