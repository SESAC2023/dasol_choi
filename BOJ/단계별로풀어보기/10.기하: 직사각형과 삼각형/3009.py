#네 번째 점

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
  res_x = x3
elif x2 == x3:
  res_x = x1
else:
  res_x = x2

if y1 == y2:
  res_y = y3
elif y2 == y3:
  res_y = y1
else:
  res_y = y2

print(res_x, res_y)
