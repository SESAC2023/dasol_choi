# 덱

import sys
input = sys.stdin.readline

def deque(command, num=None):
  global q
  if command == "push_front":
    q = [num] + q
  if command == "push_back":
    q.append(num)
  if command == "pop_front":
    if len(q) == 0: print(-1)
    else: 
      print(q[0])
      q = q[1:]
  if command == "pop_back":
    if len(q) == 0: print(-1)
    else: 
      print(q[-1])
      q = q[:-1]
  if command == "size": print(len(q))
  if command == "empty":
    if len(q) == 0: print(1)
    else: print(0)
  if command == "front":
    if len(q) == 0: print(-1)
    else: print(q[0])
  if command == "back":
    if len(q) == 0: print(-1)
    else: print(q[-1])

n = int(input())

q = []
for _ in range(n):
  x = list(input().split())
  if len(x) == 2:
    deque(x[0], int(x[1]))
  else: deque(x[0])
