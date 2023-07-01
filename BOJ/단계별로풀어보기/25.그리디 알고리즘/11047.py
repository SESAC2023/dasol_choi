#동전 0

num, price = map(int, input().split())
coins = [int(input()) for _ in range(num)]
coins.sort(reverse=True)

cnt= 0
for i in range(num):
        if price / coins[i] <1:
                continue
        if price / coins[i] == 1:
                cnt += 1
                break
        else:
                cnt += price // coins[i]
                price = price % coins[i]
print(cnt)    
