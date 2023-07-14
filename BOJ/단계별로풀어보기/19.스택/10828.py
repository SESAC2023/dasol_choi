# 스택

n = int(input())
cmd = list(input() for _ in range(n))
li = []
for x in cmd:
    if 'push' in x:
        c, num = x.split()
        li.append(int(num))
    elif x == 'top':
      print(li[-1] if len(li) > 0 else -1)       
    elif x == 'size':
        print(len(li))
    elif x == 'empty':
      print(1 if len(li)==0 else 0)
    elif x == 'pop':
      print(li.pop() if len(li) > 0 else -1)
