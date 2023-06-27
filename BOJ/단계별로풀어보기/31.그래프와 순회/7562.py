#나이트의 이동

import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

dx = [2, -2, 2, -2, 1, -1, 1, -1]
dy = [1, 1, -1, -1, 2, 2, -2, -2]

t = int(input())
for _ in range(t):
  l = int(input())
  graph = [[0]*l for i in range(l)]
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())
  q = deque()
  q.append((start_x, start_y))
  while q:
    x, y = q.popleft()
    if (x, y) == (end_x, end_y):
      print(graph[x][y]) 
      break
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >=l or ny < 0 or ny >=l:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
