#듣보잡

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_dict = {}
for _ in range(n):
  name = input().rstrip()
  n_dict[name] = 1

res_list = []
for _ in range(m):
  name = input().rstrip()  
  if name in n_dict:
    res_list.append(name)
    
print(len(res_list))
for x in sorted(res_list):
  print(x)
