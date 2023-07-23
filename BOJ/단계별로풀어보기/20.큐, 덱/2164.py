# 카드2

import sys
from collections import deque
n = int(sys.stdin.readline())
card = list(i for i in range(1, n+1))
Q = deque(card)
while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())       
print(Q[0])
