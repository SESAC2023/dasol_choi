#인사성 밝은 곰곰이

import sys
input = sys.stdin.readline
n = int(input())

words = [input().strip() for _ in range(n)]

cnt = 0
temp = set()
for word in words:
  if word == 'ENTER':
    cnt += len(temp)
    temp = set()
  else:
    temp.add(word)
cnt += len(temp)
print(cnt)
