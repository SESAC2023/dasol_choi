#상수

# 문자열로 바꿔 풀기
a, b = input().split()
new_a = ''
new_b = ''
for i in range(len(a)):
  new_a += a[-1-i]
  new_b += b[-1-i]
result = max(int(new_a), int(new_b))
print(result)


# 숫자로 풀기
a, b = map(int, input().split())
new_a = (a%10)*100 + ((a - ((a//100)*100))//10)*10 + a//100
new_b = (b%10)*100 + ((b - ((b//100)*100))//10)*10 + b//100
print(max(new_a, new_b))
