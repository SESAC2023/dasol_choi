#나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())

members = []
for i in range(n):
  age, name = input().split()
  members.append((int(age), i, name))

members.sort(key=lambda x:(x[0], x[1]))
for x in members:
  print(x[0], x[2])
