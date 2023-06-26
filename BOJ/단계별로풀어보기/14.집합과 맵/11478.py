import sys
input = sys.stdin.readline

s = input().rstrip()
len_s = len(s)

res = set()
for i in range(len_s):
  for j in range(len_s):
    res.add(s[i:(i+j+1)])
  
print(len(res))
