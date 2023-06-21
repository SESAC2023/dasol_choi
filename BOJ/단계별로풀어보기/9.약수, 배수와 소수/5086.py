#배수와 약수
# a가 b의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력, 마지막 줄에는 0이 2개

while True:
  a, b = map(int, input().split(" "))
  
  if a == b == 0: 
    break

  if b % a == 0 :
    print("factor")
  elif a % b == 0:
    print("multiple")
  else:
    print("neither")
