# 짐 챙기는 숌 (그리디 알고리즘)

n, m = map(int, input().split())

if n == 0: print(0)  # 책이 없으면 0을 출력
else:
  weights = list(map(int, input().split()))
  temp = 0
  box_cnt = 0
  for w in weights:
    temp += w  # 박스에 일단 책 넣기
    # 박스에 책 무게가 정확히 맞아 떨어지면 박스 포장 후 새 박스 준비
    if temp == m:  
      box_cnt += 1
      temp = 0
      continue
    # 책 무게가 더 무거울 경우, 마지막에 넣은 책을 빼고 박스 포장 + 뺀 책은 새 박스에 넣기
    if temp > m:
      box_cnt += 1
      temp = w
      continue
  # 책이 남김 없이 싸졌다면 현재 박스 출력
  if temp == 0:
    print(box_cnt)
  # 책이 남았다면 박스 하나 더 추가
  else: 
    print(box_cnt + 1)
