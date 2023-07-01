#ATM

#시간 초과
import sys
input = sys.stdin.readline

n = int(input())
pi = list(map(int, input().split()))

def counting(order):
  cnt = 0
  for i in range(n):
    cnt += pi[order[i]-1] * (n-i)
  return cnt

visited = [False]*(n+1)

order = []
def dfs():
  global min_sum
  if len(order) == n:
    cnt = counting(order)
    if cnt < min_sum:
      min_sum = cnt
    return 
  for i in range(1, n+1):
    if not visited[i]:
      visited[i] = True
      order.append(i)
      dfs()
      order.pop()
      visited[i] = False
min_sum = 1e9
dfs()
print(min_sum)
