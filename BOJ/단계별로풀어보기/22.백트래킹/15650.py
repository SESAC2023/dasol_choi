# N과 M(2)

import sys
input = sys.stdin.readline
#n까지 자연수 중 m개 고른 경우의 수(오름차순)

def dfs():
    if len(s) == m:
        if sorted(s) not in ss:
          ss.append(sorted(s))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False           

n, m = map(int, input().split())
s = []
ss = []
visited = [False] * (n+1)

dfs()
for s in ss:
  print(' '.join(map(str, s)))
