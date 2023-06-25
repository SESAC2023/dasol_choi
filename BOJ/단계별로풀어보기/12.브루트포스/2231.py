#분해합

n = int(input())

# 숫자가 들어왔을 때 생성자를 return하는 함수
def check(x):
  res = x
  x_str = str(x)
  for i in range(len(x_str)):
    res += int(x_str[i])
  return res

# 처음으로 등장하는(가장 작은) 생성자 출력
for i in range(n):
  if check(i) == n:
    print(i)
    break
else: print(0)
