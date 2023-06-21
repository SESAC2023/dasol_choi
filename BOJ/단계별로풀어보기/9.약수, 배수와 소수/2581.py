#소수

m = int(input())
n = int(input())

prime_list = []
for num in range(m, n+1):
  prime_num = True  #해당 숫자의 소수 여부 저장 변수
  if num == 1:  #숫자가 1일 경우 스킵
    continue
  for i in range(2, num):  #숫자가 소수이면 list에 넣기
    if num % i == 0:
      prime_num = False
  if prime_num == True:
    prime_list.append(num)

if len(prime_list) == 0:
  print(-1)
else:
  print(sum(prime_list))
  print(min(prime_list))
