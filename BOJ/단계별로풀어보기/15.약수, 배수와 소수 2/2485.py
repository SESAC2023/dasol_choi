#가로수

# 런타임 에러!!!!
import sys
input = sys.stdin.readline
n = int(input())

trees = [int(input()) for _ in range(4)]

if trees[0] != 1:
  min_gap = trees[0]
else: min_gap = 1e9

for i in range(n-1):
  gap = trees[i+1] - trees[i]
  if gap < min_gap:
    min_gap = gap

correct_num = ((trees[-1]-trees[0])//min_gap) + 1            
print(correct_num - len(trees))
