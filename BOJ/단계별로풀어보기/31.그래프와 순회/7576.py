#토마토


# 시간 초과!!!!!!!!!!!!!!!!!!!!!!!ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
col, row = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(row)]

count1 = 0  # 0의 개수
possible = True  # 막힌 0의 개수 = 토마토가 모두 익을 수 있는지 여부
q = deque() # 탐색시작 토마토 좌표(원소가 1인 좌표)
for i in range(row):
  for j in range(col):
    if graph[i][j] == 1:
        q.append((i, j))
    if graph[i][j] == 0:
      count1 += 1 # 0의 개수 count
      temp = False # 상하좌우에 -1이 아닌 수(0 or 1)가 하나라도 있는지
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or nx >=row or ny < 0 or ny >= col:
          continue
        if graph[nx][ny] == 0 or graph[nx][ny] == 1:
          temp = True
          break
      if temp == False:
        possible = False

if count1 == 0:
  print(0)  # 모든 토마토가 익어있는 경우
elif possible == False:
  print(-1)  # 토마토가 모두 익지 못하는 상황(0이 고립된 상황)
else:
  tomatos_num = 0 #토마토 익는 숫자 세기(0->1)
  day = 0  #날짜 세기
  v = False
  while tomatos_num != count1:
    for _ in range(len(q)):
      x, y = q.popleft()
      temp = 0
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=row or ny<0 or ny>=col:
          continue
        if graph[nx][ny] == -1:
          continue
        if graph[nx][ny] == 0:
          graph[nx][ny] = 1
          tomatos_num += 1
          q.append((nx, ny))
    day += 1  
  print(day)
