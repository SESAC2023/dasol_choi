# 행렬 곱셈

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

# 행렬 곱셈 함수
def matrix_multiply(a, b):
    result = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for l in range(m):
                result[i][j] += a[i][l] * b[l][j]

    return result

result = matrix_multiply(a, b)
for row in result:
    print(' '.join(map(str, row)))
