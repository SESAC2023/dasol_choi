#약수들의 합

while True:
  
  n = int(input())
  
  if n == -1:  # 종료 조건
    break

  else:
    factors= []
    for i in range(1, n):
      if n % i == 0:
        factors.append(i)
    if sum(factors) == n:
      print(f"{n} = ", end="")
      for j in range(len(factors)):
        if j == len(factors)-1:
          print(factors[j])
        else:
          print(f'{factors[j]} + ', end="")
    else: print(f'{n} is NOT perfect.')
