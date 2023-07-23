# 요세푸스 문제 0

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
people = deque([i for i in range(1, n+1)])
order = []
i = 1
while people:
  if i == k:
      order.append(people.popleft())
      i = 1
  else: 
    people.append(people.popleft())
    i += 1

res = "<" + ", ".join(str(num) for num in order) + ">"
print(res)
