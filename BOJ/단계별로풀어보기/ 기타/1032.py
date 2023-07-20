# 명령 프롬프트 

n = int(input())
file_names = [input() for _ in range(n)]

standard = file_names[0]
res = ''

for i in range(1, len(file_names)):
  for j in range(len(standard)):
    if file_names[i][j] == standard[j]:
      res += standard[j]
    else: res += '?'
  standard = res
  res = ''

print(standard)
