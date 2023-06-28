#팩토리얼

import sys
input = sys.stdin.readline

n = int(input())
res = 1
while n > 0:
    res *= n
    n -= 1
print(res)
