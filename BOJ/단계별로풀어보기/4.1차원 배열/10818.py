#최소,최대

n = int(input())
a = list(map(int, input().split()))

max = -1000000
min = 1000000
for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max)
