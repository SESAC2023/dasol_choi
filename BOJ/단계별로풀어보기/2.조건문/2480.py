#주사위 세개

a = list(map(int, input().split()))

if a[0] == a[1] ==a[2] :
    reward = 10000+a[0]*1000
elif a[0] == a[1] or a[0] == a[2]:
    reward =1000+a[0]*100
elif a[1] == a[2]:
    reward =1000+a[1]*100
else:
    reward = max(a)*100
  
print(reward)
