curr_h, curr_m = map(int, input().split())
cooking_m = int(input())

total_finish_m = curr_h*60 + curr_m + cooking_m

finish_h = total_finish_m//60
finish_m = total_finish_m%60

if finish_h >= 24:
  finish_h = finish_h - 24

print(finish_h, finish_m)
