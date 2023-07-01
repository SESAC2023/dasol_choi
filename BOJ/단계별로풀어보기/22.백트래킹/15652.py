# N과 M(4)

import sys
input = sys.stdin.readline
#n까지 자연수 중 m개 고른 경우의 수(중복허용, 오름차순)

n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)
