#다이얼

word = input()

tel_dict = {'ABC': 2, 'DEF':3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ' : 9}

t = 0
for letter in word:
  for key, value in tel_dict.items():
    if letter in key:
      num = tel_dict[key]
  t += (num+1)

print(t)
