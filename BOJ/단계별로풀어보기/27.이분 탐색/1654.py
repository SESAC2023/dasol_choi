# 랜선 자르기
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

minn = 1
maxx = max(lans)
result = 0

while minn <= maxx:
    mid = (minn + maxx) // 2
    count = 0
    for lan in lans:
        count += lan // mid
    
    if count >= n:
        result = mid
        minn = mid + 1
    else:
        maxx = mid - 1

print(result)
