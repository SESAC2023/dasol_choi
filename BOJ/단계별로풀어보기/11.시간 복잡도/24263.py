# 알고리즘 수업 - 알고리즘의 수행 시간 2


#MenOfPassion(A[], n) {
#    sum <- 0;
#    for i <- 1 to n
#        sum <- sum + A[i]; # 코드1
#    return sum;
#}
# 이 함수는 전체 원소의 합을 구하는 프로그램
# f(n) = 1(대입) + n*( 1(대입) + 1(덧셈) + 1(대입) ) = 1 + 3n
# O(f(n)) = n


n = int(input())
print(n)
print(1)
