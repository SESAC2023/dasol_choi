#벌집

# 1 7 19 37 61
# 13은 방3개, 58은 방 5개

n = int(input())

num = 1
idx = 1
while n > num:
  num = num + (6*idx)
  idx += 1

print(idx)
