h, m = map(int, input().split(" "))
total_m = h*60 + m 
alarm_m = total_m - 45

if alarm_m < 0:
  new_h = 23
  new_m = 60 + alarm_m
else:
  new_h = alarm_m//60
  new_m = alarm_m%60

print(new_h, new_m)
