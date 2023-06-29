# 토마토

import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
col, row, h = map(int, input().split())

# 6가지 방향에 대한 정의: 상, 하, 좌, 우, 위, 아래
dz = [0, 0, 0, 0, 1, -1]  # 높이 방향
dx = [-1, 1, 0, 0, 0, 0]  # 행 방향
dy = [0, 0, -1, 1, 0, 0]  # 열 방향

graph = []  # 그래프 입력
for _ in range(h):
  graph.append([list(map(int, input().split())) for _ in range(row)])
visited = [[[-1] * col for _ in range(row)] for _ in range(h)]  # 방문처리 배열

q = deque()  # 탐색 시작 토마토 좌표(원소가 1인 좌표) 모두 큐에 넣기
for k in range(h):
  for i in range(row):
    for j in range(col):
      if graph[k][i][j] == 1:
        q.append((k, i, j))
        visited[k][i][j] = 0
   
while q:  # q가 빌 때까지 BFS 수행
  z, x, y = q.popleft()  # 익은 토마토 (z, x, y)의 위치 구하기
  # 현재 위치에서 인접한 6가지 공간 확인
  for i in range(6):
    nz = z + dz[i]
    nx = x + dx[i]
    ny = y + dy[i]
    # 공간을 벗어난다면 무시
    if nx < 0 or nx >= row or ny < 0 or ny >= col or nz < 0 or nz >= h:
      continue
    # 벽이라면 무시
    if graph[nz][nx][ny] == 1:
      continue
     # 안 익은 토마토가 있다면, 익도록 처리
    if graph[nz][nx][ny] == 0:
      graph[nz][nx][ny] = 1  
      visited[nz][nx][ny] = visited[z][x][y] + 1  # 이전 위치까지의 최단 거리 + 1
      q.append((nz, nx, ny))

possible = True
answer = 0  # 최댓값 계산
for k in range(h):
  for i in range(row):
    for j in range(col):
        # 도착 불가능하면서, 벽이 아닌 경우
        if visited[k][i][j] == -1 and graph[k][i][j] != -1:
            possible = False  # 모든 위치를 익게 만드는 것이 불가능
        answer = max(answer, visited[k][i][j])  # answer에는 최댓값이 담김

if possible:
    print(answer)
else:
    print(-1)
