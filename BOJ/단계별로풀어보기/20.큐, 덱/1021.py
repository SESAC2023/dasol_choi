# 회전하는 큐 

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
pos = list(map(int, input().split()))

q = deque([i for i in range(1, n+1)])
cnt = 0
for x in pos:
  while True:
    if q.index(x) == 0:
      q.popleft()
      break
    if q.index(x) <= len(q)/2:
      q.append(q.popleft())
      cnt += 1
    else:
      q.appendleft(q.pop())
      cnt += 1
print(cnt)
