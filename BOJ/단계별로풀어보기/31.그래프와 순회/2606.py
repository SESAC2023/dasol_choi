#바이러스

import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 노드의 개수(n), 간선의 개수(m), 시작 노드(r)
n = int(input())
m = int(input())
r =1

# 인접 리스트
graph = [[] for i in range(n + 1)]
# 각 노드에 대한 방문 여부
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    # 양방향 간선이기 때문에
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
def dfs(x):
  global cnt
  visited[x] = True
  cnt += 1
  for y in graph[x]:
    if not visited[y]:
      dfs(y)

dfs(r)
print(cnt-1)
