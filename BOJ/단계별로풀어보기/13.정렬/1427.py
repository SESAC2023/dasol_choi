#소트인사이드

import sys
input = sys.stdin.readline

n = input()

nums = [x for x in n]
nums.sort(reverse=True)
for x in nums:
  print(x, end="")
