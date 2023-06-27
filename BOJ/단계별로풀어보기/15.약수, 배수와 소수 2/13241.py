#최소공배수

import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())

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
  
print(func(a, b))
