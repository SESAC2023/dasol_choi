# 큐 2

import sys
from collections import deque
ip = sys.stdin.readline
n = int(ip())
Q = deque()
for _ in range(n):
    a = ip().split()
    if a[0] == 'push':
        Q.append(a[1])
    if a[0] == 'pop':
        print(Q.popleft() if Q else -1)
    if a[0] == 'size':
        print(len(Q))
    if a[0] == 'empty':
        print(0 if Q else 1)
    if a[0] == 'front':
        print(Q[0] if Q else -1)
    if a[0] == 'back':
        print(Q[-1] if Q else -1)
