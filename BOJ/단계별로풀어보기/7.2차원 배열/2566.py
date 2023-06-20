#최댓값

matrix= []  
for _ in range(9):
  matrix.append(list(map(int, input().split())))

max = 0
for i in range(9):
    for j in range(9):
      if matrix[i][j] >= max:
        max =  matrix[i][j]
        idx = [i+1, j+1]

print(max)
print(idx[0], idx[1])
