# 제로

import sys
i = sys.stdin.readline
k= int(i())
stack = []
for _ in range(k):
    a = int(i())
    stack.pop() if  a == 0 else stack.append(a)
print(sum(stack))
