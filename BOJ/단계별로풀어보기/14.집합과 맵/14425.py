#문자열 집합

n, m = map(int, input().split())

s = {}
for _ in range(n):
  word = input()
  s[word] = 1

cnt = 0
for _ in range(m):
  word = input()
  try: 
    cnt += s[word]
  except:
    pass

print(cnt)
