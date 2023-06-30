# N과 M(1)
# n까지 자연수 중 m개 고른 경우의 수

import sys
input = sys.stdin.readline

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
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
visited = [False] * (n+1)

dfs()
