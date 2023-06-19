#알파벳 찾기

s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for x in alpha:
    print(s.find(x), end=' ')
  
# for i in range(len(alpha)):
#   for j in range(len(s)):
#     if alpha[i] == s[j]: 
#       print(j, end=" ") 
#       break
#   else: print(-1, end=" ")
