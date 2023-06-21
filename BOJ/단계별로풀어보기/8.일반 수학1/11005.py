#진법 변환 2

n, b = map(int, input().split(" "))

base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = ''
while n > 0:
    remainder = n % b
    res = base[remainder] + res
    n //= b

print(res)
