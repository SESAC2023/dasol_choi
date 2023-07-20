# 쉽게 푸는 문제

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

nums = []
for i in range(1, 46):
  for j in range(i):
    nums.append(i)

num_sum = 0
for i in range(a-1, b):
  num_sum += nums[i] 
  
print(num_sum)
