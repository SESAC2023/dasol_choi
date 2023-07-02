#회의실 배정

import sys
input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
  s, e = map(int, input().split())
  times.append((s, e))

times.sort(key= lambda x: (x[1], x[0]))
end = 0
cnt = 0
for s, e in times:
  if s >= end:
    end = e
    cnt +=1
print(cnt)
print(max_cnt)
