#크로아티아 알파벳

s = input()

letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#letters의 문자가 입력 문자열에 존재하면 온점(.)으로 변경-> lenth를 1로 변경
for letter in letters:
  s = s.replace(letter, ".")

print(len(s))
