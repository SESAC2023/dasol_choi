#별 찍기 - 7

n = int(input())

for i in range(1, n+1):
  blank = n-i 
  print(' '*blank, end='')
  print('*'*(2*i-1))

for i in range(1, n):
  blank = i 
  print(' '*blank, end='')
  print('*'*((2*n-2*i)-1))
