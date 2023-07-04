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

#---------------------------------
import sys

sys.setrecursionlimit(int(1e6))

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
selected = []  # 현재 경우에서 선택된 원소들
visited = [False] * n  # 각 원소가 선택되었는가

# cnt = 0


# depth: 현재 재귀에서 선택된 원소의 개수
def dfs(depth, now):
    global cnt
    if depth == m:
        # 실제로 현재 경우에 대하여 처리하는 부분
        for x in selected:
            print(x, end=" ")
        print()
        # cnt += 1
        return
    for i in range(now, n):
        if visited[i]:
            continue
        # 백트래킹은 3단계로 재귀 호출
        # (1) 원소 넣기
        selected.append(arr[i])
        visited[i] = True
        dfs(depth + 1, i)  # (2) 재귀 호출
        # (3) 원소 빼기
        selected.pop()
        visited[i] = False


dfs(0, 0)
# print(cnt)
