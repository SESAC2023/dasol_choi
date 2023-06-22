#세 막대

sides = sorted(list(map(int, input().split()))) #세 변의 길이 오름차순

#삼각형의 조건이 만족할 때까지 가장 길이가 큰 변을 1씩 줄이기
while sides[-1] >= (sides[0] + sides[1]):
    sides[-1] -= 1
print(sum(sides))  #만들 수 있는 가장 큰 삼각형 둘레 출력
