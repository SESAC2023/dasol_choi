#체스판 다시 칠하기

n, m = map(int, input().split())
square = []
 
for _ in range(n):
    square.append(input())
 
for i in range(n-7):
  for j in range(m-7):
    cnt1 = 0
    cnt2 = 0
    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a + b) % 2 == 0:
          if square[a][b] != 'B':
            cnt1 += 1
          if square[a][b] != 'W':
            cnt2 += 1
        else:
          if square[a][b] != 'W':
            cnt1 += 1
          if square[a][b] != 'B':
            cnt2 += 1
 
print(min([cnt1, cnt2]))
