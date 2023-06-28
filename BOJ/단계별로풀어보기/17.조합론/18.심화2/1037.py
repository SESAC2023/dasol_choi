# 약수

import sys
input = sys.stdin.readline
cnt = int(input())
primes = sorted(list(map(int, input().split())))

print(primes[0] * primes[-1])
