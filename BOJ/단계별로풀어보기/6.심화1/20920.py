# 영단어 암기는 괴로워

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
for _ in range(n):
  temp = input().rstrip()
  if len(temp) >= m:
    words.append(temp)
    
cnt_dict = {}
for word in words:
    if word in cnt_dict:
        cnt_dict[word] += 1
    else:
        cnt_dict[word] = 1
sorted_words = sorted(set(words), key=lambda x: (-cnt_dict[x], -len(x), x))

for word in sorted_words:
  print(word)
