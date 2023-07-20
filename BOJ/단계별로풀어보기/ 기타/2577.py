# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

num = a * b * c
num_dict = dict()
for i in range(10):
  num_dict[str(i)] = 0
for x in str(num):
  num_dict[x] += 1

for key, value in num_dict.items():
  print(value)
