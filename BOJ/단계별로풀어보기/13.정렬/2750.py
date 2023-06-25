#수 정렬하기

# 삽입정렬
n = int(input())

l = [int(input()) for _ in range(n)]
for _ in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
for i in l:
    print(i)
