#DFS와 BFS

import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for i in range(n + 1)]

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
  graph[i].sort()

def dfs(x):
  dfs_visited[x] = True
  print(x, end=" ")
  for y in graph[x]:
    if not dfs_visited[y]:
      dfs(y)

def bfs(x):
  q = deque([x])
  bfs_visited[x] = True 
  while q:
    v = q.popleft()
    print(v, end=" ")
    for y in graph[v]:
      if not bfs_visited[y]:
        q.append(y)
        bfs_visited[y] = True

dfs(v)
print()
bfs(v)
