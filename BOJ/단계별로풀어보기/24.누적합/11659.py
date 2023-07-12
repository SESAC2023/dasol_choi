# 구간 합 구하기 4

import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
nums = list(map(int, input().split()))  
s_list = [] 
temp = 0
for num in nums:  
  temp += num
  s_list.append(temp) 
  
for _ in range(m):
  s, e = map(int, input().split())
  new_e = s_list[e-1]
  if s == 1 :
    new_s = 0
  else: new_s =  s_list[s-2]
  print(new_e - new_s)
