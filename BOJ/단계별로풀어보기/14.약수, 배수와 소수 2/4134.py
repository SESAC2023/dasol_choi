#다음 소수

# 시간 초과!!!!!!!!!!!!!!!!!!!!!!!!
import sys
input = sys.stdin.readline
n = int(input())

def isPrime(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  else:
    return True

for _ in range(n):
  num = int(input())
  while isPrime(num)==False:
    num += 1
  print(num)
