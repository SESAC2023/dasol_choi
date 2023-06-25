#수학은 비대면강의입니다

# 연립방정식 해 구하기
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
  for j in range(-999, 1000):
     if a*i + b*j == c and d*i + e*j == f:
       print(i, j)
