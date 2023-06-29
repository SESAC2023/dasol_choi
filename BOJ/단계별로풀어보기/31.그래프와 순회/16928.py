#뱀과 사다리 게임

import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
n, m = map(int, input().split())
map = [i for i in range(0, 101)]

# 사다리 정보 추가
for _ in range(n):
  num = input().split()
  x, y = int(num[0]), int(num[1]) 
  map[x] = y
# 뱀 정보 추가
for _ in range(m):
    num = input().split()
    u, v =  int(num[0]), int(num[1])
    map[u] = v 

visited = set() 
distance = dict()

q = deque()
q.append(1) 
visited.add(1)  
distance[1] = 0  # 자기 자신까지는 0회

# BFS 수행
while q: 
  current = q.popleft() 
  if map[current] == 100:
    break
  for i in range(1, 7):
    if current + i > 100:
      continue
    next = map[current + i]
    if next not in visited:  
        visited.add(next)
        q.append(next)
        distance[next] = distance[current] + 1
    
print(distance[100])
