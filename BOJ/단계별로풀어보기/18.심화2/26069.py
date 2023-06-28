#붙임성 좋은 총총이

import sys
input = sys.stdin.readline
n = int(input())

persons = []
for _ in range(n):
  p1, p2 = input().strip().split()
  if p1 == 'ChongChong' or p2 == 'ChongChong':
    persons.append(p1)
    persons.append(p2)
  if p1 in persons or p2 in persons:
    persons.append(p1)
    persons.append(p2)

print(len(set(persons)))
