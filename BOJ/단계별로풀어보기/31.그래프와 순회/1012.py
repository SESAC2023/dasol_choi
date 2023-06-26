#유기농 배추

import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col):
  visited[row][col] = True
  for i in range(4):
    nx = row + dx[i]
    ny = col + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] == 0:
      continue
    if not visited[nx][ny]:
      dfs(nx, ny)
    
t = int(input())  # test case
for _ in range(t):
  m, n, k = map(int, input().rstrip().split())
  
  # 배추밭 격자 만들기
  graph = [[0]*m for _ in range(n)]
  visited = [[False]*m for _ in range(n)]

  # 배추가 있는 좌표축 표시
  for _ in range(k):
    col, row = map(int, input().rstrip().split())
    graph[row][col] = 1

  answer = 0  # 인접한 배추들 묶음 개수
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        continue
      if not visited[i][j]:
        answer += 1
        dfs(i, j)
  print(answer)
