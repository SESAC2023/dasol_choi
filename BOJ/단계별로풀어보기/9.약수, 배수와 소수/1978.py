#소수 찾기

n = int(input())
num_list = list(map(int, input().split(" ")))

res = 0
for num in num_list:
  prime_num = True
  if num == 1:
    continue
  for i in range(2, num):
    if num % i == 0:
      prime_num = False
  if prime_num == True:
    res += 1
print(res)
