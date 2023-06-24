#알고리즘 수업 - 깊이 우선 탐색 1

import sys
# 재귀 깊이 한도 해제
sys.setrecursionlimit(int(1e6))
# 빠른 입력받기
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]

# 그래프 만들기(무방향 그래프)
for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

# 그래프 정렬(오름차순)
for i in range(1, n+1):
  graph[i].sort()

visited = [False]*(n+1)  # 방문처리 저장 변수
answer = [0] * (n+1) # 방문순서 저장변수
def dfs(x):
  global order
  visited[x] = True
  answer[x] = order
  order += 1
  for y in graph[x]:
    if not visited[y]:
      dfs(y)

order = 1
dfs(r)

for i in range(1, n+1):
  print(answer[i])
