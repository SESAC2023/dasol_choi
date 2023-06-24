#알고리즘 수업 - 알고리즘의 수행 시간 3

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 이 함수는 모든 원소에 대해 다른 모든 원소를 곱한 것의 합을 구하는 프로그램
# 2중 반복문 -> O(n**2)

n = int(input())

print(n*n)
print(2)
