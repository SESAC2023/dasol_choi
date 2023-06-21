#중앙 이동 알고리즘

# 2*2, 3*3, 5*5, 9*9, 17*17, 33*33, ....
n = int(input())

res = 2  #초기 세팅
for i in range(1, n+1):
  res = (res+2**(i-1))
  
print(res**2)
