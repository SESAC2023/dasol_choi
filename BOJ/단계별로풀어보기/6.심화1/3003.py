#킹, 퀸, 룩, 비숍, 나이트, 폰

pieces = list(map(int, input().split()))
standard = [1,1,2,2,2,8] 

for i in range(len(pieces)):
    print(standard[i]-pieces[i], end=' ')
