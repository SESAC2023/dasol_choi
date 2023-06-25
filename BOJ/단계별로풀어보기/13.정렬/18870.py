#좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
xs = list(map(int, input().split()))
sorted_xs = sorted(set(xs))

xs_dict = {}
for i in range(len(sorted_xs)):
  xs_dict[sorted_xs[i]] = i 

for x in xs:
  print(xs_dict[x], end=" ")
