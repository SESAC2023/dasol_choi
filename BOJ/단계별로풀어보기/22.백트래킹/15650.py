# N과 M(2)

import sys
input = sys.stdin.readline
#n까지 자연수 중 m개 고른 경우의 수(오름차순)

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
