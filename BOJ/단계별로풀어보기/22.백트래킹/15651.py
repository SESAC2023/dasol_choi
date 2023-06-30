# N과 M(3)

import sys
input = sys.stdin.readline
#n까지 자연수 중 m개 고른 경우의 수(중복포함)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False           

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()
