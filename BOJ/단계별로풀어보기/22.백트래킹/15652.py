# N과 M(4)

#시간초과
import sys
input = sys.stdin.readline
#n까지 자연수 중 m개 고른 경우의 수(중복허용, 오름차순)

def dfs():
    if len(s) == m:
        temp = tuple(sorted(s))
        ss.add(temp)
        return
    for i in range(1, n+1):
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False           

n, m = map(int, input().split())
s = []
ss = set()
visited = [False] * (n+1)

dfs()
for s in sorted(ss):
  print(' '.join(map(str, s)))
