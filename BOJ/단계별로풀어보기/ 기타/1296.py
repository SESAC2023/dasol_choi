# 팀 이름 정하기

import sys
input = sys.stdin.readline

def cnt(word):
  l, o, v, e = 0, 0, 0, 0
  for letter in word:
    if letter == 'L': l += 1
    if letter == 'O': o += 1
    if letter == 'V': v += 1
    if letter == 'E': e += 1
  return l, o, v, e

l, o, v, e = 0, 0, 0, 0
name = input().strip()
a, b, c, d = cnt(name)
l += a 
o += b
v += c
e += d

n = int(input())
res_dict = dict()
teams = list(input().strip() for _ in range(n))
for team in teams:
  a, b, c, d = cnt(team)
  L = l + a 
  O = o + b
  V = v + c
  E = e + d
  res = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
  res_dict[team] = res

print(sorted(res_dict.items(), key=lambda item:[-item[1], item[0]])[0][0])
