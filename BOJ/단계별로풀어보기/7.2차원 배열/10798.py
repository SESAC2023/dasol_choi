#세로읽기

import sys

matrix= []
max_len = 0
for _ in range(5):
  temp = list(sys.stdin.readline().rstrip())
  if len(temp) > max_len:
    max_len = len(temp)
  matrix.append(temp)

for i in range(max_len):
    for j in range(5):
      try:
        print(matrix[j][i], end='')
      except : continue
