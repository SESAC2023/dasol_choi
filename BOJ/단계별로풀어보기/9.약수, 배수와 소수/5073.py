#삼각형과 세 변

while True:
  a, b, c = map(int, input().split())
  #while문 종료조건
  if a == b == c == 0: 
    break
  #삼각형 조건 만족하지 못하는 경우
  lenths = sorted([a, b, c])
  if lenths[-1] >= (lenths[0] + lenths[1]):
    print("Invalid")
    continue
  #삼각형 만족하는 경우 - 세 변의 길이에 따라 정의  
  if a == b == c:
    print("Equilateral")
  elif a == b or b == c or a == c:
    print("Isosceles")
  else:
    print("Scalene")
