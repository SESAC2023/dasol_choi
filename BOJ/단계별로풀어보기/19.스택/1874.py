# 스택 수열

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = deque(list(int(input()) for _ in range(n)))

stack = []
operations = []
for i in range(1, n+1):
  stack.append(i)
  operations.append('+')
  while True:
    if len(stack) == 0:
      break
    if stack[-1] == nums[0]:
      stack.pop()
      operations.append('-')
      nums.popleft()
    else: break

if not stack:
  for oper in operations:
    print(oper)
else:
  print('NO')
