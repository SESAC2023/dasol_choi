#행렬 덧셈

n, m = map(int, input().split())

a = []
for _ in range(n):
  temp = list(map(int, input().split()))
  a.append(temp)
  
b = []
for _ in range(n):
  temp = list(map(int, input().split()))
  b.append(temp)

for i in range(n):
    for j in range(m):
      print(a[i][j] + b[i][j], end=" ")
