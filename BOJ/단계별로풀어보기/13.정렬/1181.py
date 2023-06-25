#단어 정렬

import sys
input = sys.stdin.readline

n = int(input())

words = []
for _ in range(n):
  word = input().strip()
  words.append((len(word), word))

words = sorted(list(set(words)))
for x in words:
  print(x[1])
