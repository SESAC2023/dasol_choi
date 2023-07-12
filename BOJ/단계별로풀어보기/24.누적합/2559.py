# 수열
#K는 1과 N 사이의 정수

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
temps = list(map(int, input().split()))
temps_sum = [] 
s = 0
for temp in temps:  
  s += temp
  temps_sum.append(s) 

if k == n:
  print(temps_sum[-1])
elif k == 1:
  print(max(temps))
else:
  max_temp = 0
  for i in range(0, n-k+1):
    s, e = i, i+k-1
    new_e = temps_sum[e]
    if s == 0:
      new_s = 0
    else: new_s = temps_sum[s-1]
    x = new_e - new_s
    if x > max_temp:
      max_temp = x
  print(max_temp)
