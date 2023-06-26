#숫자 카드 2

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_dict = {}
for num in n_list:
  if num in n_dict:
    n_dict[num] += 1
  else:
    n_dict[num] = 1
  
m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
  try:
    print(n_dict[num], end=" ")
  except:
    print(0, end=" ")
