#회의실 배정

# 시간초과ㅠㅠ
import sys
input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
  s, e = map(int, input().split())
  times.append((s, e))

times.sort()

max_cnt = 0
for i in range(n):
  end = times[i][1]
  cnt = 1
  for j in range(i+1, n):
    if times[j][0] >= end:
      end = times[j][1]
      cnt +=1
  if cnt > max_cnt:
    max_cnt = cnt
print(max_cnt)
