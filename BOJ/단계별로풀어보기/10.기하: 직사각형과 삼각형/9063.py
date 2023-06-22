#대지

n = int(input())

# min(), max() 함수 활용가능하지만 그냥 구현해 봄
x_min, x_max = 10000, -10000
y_min, y_max = 10000, -10000
for _ in range(n):
  x, y = map(int, input().split())
  if x < x_min:
    x_min = x
  if x > x_max:
    x_max = x
  if y < y_min:
    y_min = y
  if y > y_max:
    y_max = y
  
print((x_max-x_min)*(y_max-y_min))
