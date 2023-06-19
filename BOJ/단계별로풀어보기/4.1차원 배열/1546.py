#평균

n = int(input())
a = list(map(int, input().split()))

new_a = []
for i in a:
    new_a.append(i / max(a)*100)
print(sum(new_a)/len(a))
