import sys

sys.setrecursionlimit(int(1e6))

n = int(input())
data = list(map(int, input().split()))  # [3, 4, 5]
operators = list(map(int, input().split()))  # [+개수, -개수, *개수, /개수]
m = n - 1  # 선택할 총 연산자 수

selected = []  # 현재 경우에서 선택된 원소들

min_value = 1e10
max_value = -1e10


# depth: 현재 재귀에서 선택된 원소의 개수
def dfs(depth):
    global min_value, max_value
    if depth == m:
        # 실제로 현재 경우에 대하여 처리하는 부분
        total = data[0]
        for i in range(m):
            current = selected[i]
            if current == 0:  # 더하기
                total += data[i + 1]
            elif current == 1:  # 빼기
                total -= data[i + 1]
            elif current == 2:  # 곱하기
                total *= data[i + 1]
            else:  # 나누기
                if total < 0:
                    total = -((-total) // data[i + 1])
                else:
                    total //= data[i + 1]
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return
    for i in range(4):
        if operators[i] == 0:
            continue
        # 해당 연산자가 아직 더 쓰일 수 있다면
        # 백트래킹은 3단계로 재귀 호출
        # (1) 원소 넣기
        operators[i] -= 1
        selected.append(i)
        # i == 0은 '+', i == 1은 '-', i == 2는 '*', i == 3은 '/'
        dfs(depth + 1)  # (2) 재귀 호출
        # (3) 원소 빼기
        operators[i] += 1
        selected.pop()


dfs(0)
print(max_value)
print(min_value)
