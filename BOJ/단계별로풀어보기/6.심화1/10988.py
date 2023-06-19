#팰린드롬인지 확인하기

s = input()

for i in range(len(s)//2):
  if s[i] != s[-(i+1)]:
    print(0)
    break
else:
  print(1)
