#대칭 차집합

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

res_a = a_set - (a_set & b_set) 
res_b = b_set - (a_set & b_set) 
print(len(res_a) + len(res_b))
