#색종이

n = int(input())

paper = [[0] * 100 for _ in range(100)]  # 100x100 흰 배경

# 검은 색종이 칠하기 = 검은 색종이 위치의 원소를 0에서 1로 변경
for _ in range(n):
  col, row = map(int, input().split(" "))
  for i in range(row, row+10):
    for j in range(col, col+10):
      paper[i-1][j-1] = 1

cnt = 0  # 검은색 면적 구하기 = 이차원 배열 paper에서 1의 값의 합 구하기
for row in paper:
  for num in row:
    cnt += num
print(cnt)
