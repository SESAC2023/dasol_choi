#진법 변환

n, b = input().split(" ")
base_dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35} 

res = 0
for i in range(len(n)):
  # 수의 첫번째 자리부터 진법 변환 - 주어진 수가 문자인지 숫자인지 먼저 확인 
  if n[i].isdigit():  # 주어진 수가 숫자이면 숫자 그대로 사용
    num = int(n[i])
  else:  # 주어진 수가 문자이면 숫자로 변경
    num = base_dict[n[i]]
  res += (num*int(b)**(len(n)-1-i))  # 진법 변환
print(res)

#--------------------------------------------------
# 더 간단한 코드 살펴보기
# N, b = input().split()
# ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# N = N[::-1]
# result = 0
# for i,n in enumerate(N):
#     result += (int(b)**i)*(ary.index(n))
# print(result)

# 한 줄 함수로 출력
# n, b = input().split()
# print(int(n, base=int(b)))

#--------------------------------------------------
# dictionary = dict()
# for i in range(10):
#     dictionary[str(i)] = i
# for i in range(26):
#     char = chr(i + ord('A'))  # char는 차례대로 "A"부터 "Z"까지 순회
#     dictionary[char] = i + 10

# n, b = input().split()  # 입력 문자열 N
# b = int(b)  # B진법

# n = n[::-1]  # 0제곱부터 보기 위해서 문자열 뒤집기
# answer = 0
# for i in range(len(n)):  # 각 자리마다 확인하며
#     x = dictionary[n[i]]  # 현재 문자열을 수로 바꾼 값
#     y = b**i  # 현재 곱해질 수(제곱 수)
#     answer += (x * y)
# print(answer)
