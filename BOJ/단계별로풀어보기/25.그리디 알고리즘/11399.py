#ATM

import sys
input = sys.stdin.readline

n = int(input())
pi = sorted(list(map(int, input().split())))

res = 0
cnt = 0
for x in pi:
  cnt += x
  res += cnt
print(res)
