#나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

notes = {}  #포켓몬 도감
for i in range(n):
  name = input().rstrip()
  notes[name] = i+1
  notes[str(i+1)] = name

for _ in range(m):
  quiz = input().rstrip()
  print(notes[quiz])
