#오븐 시계

h, m = map(int, input().split())
cooking_m = int(input())

total_m = h * 60 + m + cooking_m
finish_h = total_m // 60
finish_m = total_m % 60

if finish_h >= 24:
  finish_h = finish_h - 24

print(finish_h, finish_m)
