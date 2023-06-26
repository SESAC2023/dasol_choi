#최소공배수 

import sys
input = sys.stdin.readline

n = int(input())

def func(a, b):
  max_num = max(a, b)
  min_num = min(a, b)
  num = max_num
  cnt = 2
  while True:
    if num % min_num == 0:
      break
    else: 
      num = (max_num * cnt)
      cnt += 1
  return num
  
for _ in range(n):
  a, b = map(int, input().strip().split())
  print(func(a, b))
