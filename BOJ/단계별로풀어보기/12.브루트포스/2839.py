#설탕배달

n = int(input())

num_5 = n//5  #5의 배수를 빼 볼 수 있는 개수

# 5의 배수를 최대로 뺄 수 있는 케이스부터 먼저 탐색 -> 5의 배수 하나를 빼는 케이스까지 탐색
for i in range(num_5, 0, -1):
  cnt = i
  new_n = n - (5*i)
  if new_n % 3 ==0:
    cnt += (new_n//3)
    print(cnt)
    break
  else:
    continue
# 5의 배수를 먼저 탐색했을 때 딱 떨어지지 않으면 3의 배수인지 확인
else: 
  if n % 3 == 0:
    print(n//3)
  # 모두 해당되지 않는다면 딱 떨이지지 않는 수라는 의미로 -1 출력
  else:
    print(-1)
