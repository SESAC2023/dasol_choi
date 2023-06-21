#달팽이는 올라가고 싶다

a, b, v = map(int, input().split())

day = (v-a)/(a-b)+1  # 막대기 높이 / 하루동안 올라가는 높이
# 일 수 출력 -> 올림
if day > int(day):
  day = int(day) + 1
print(int(day))
