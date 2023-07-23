#프린터 큐

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  importance = deque((i, val) for i, val in enumerate(list(map(int, input().split()))))
  cnt = 0
  while True:
    cur = importance.popleft()
    if any(cur[1] < x[1] for x in importance):
      importance.append(cur)
    else:
      cnt += 1
      if cur[0] == m:
        break 
  print(cnt)
