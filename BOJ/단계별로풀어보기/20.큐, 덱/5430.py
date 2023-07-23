# AC

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  functions = input().rstrip()
  n = int(input())
  try:
    nums = deque(map(int, input().rstrip()[1:-1].split(',')))
  except: 
    nums = deque()  # 빈 리스트가 들어올 경우, 예외처리

  is_reverse = 0  # 뒤집기 여부
  for func in functions:
    if func == "R":
      # 현재 뒤집기 상태에서 다시 뒤집기
      if is_reverse: is_reverse = False
      else: is_reverse = True
    elif func == "D":
      if len(nums) == 0:
        print('error')
        break
      else:  # 정방향이면 앞에 값 버리고, 역방향이면 뒤에 값 버리기
        if is_reverse == False:
          nums.popleft()
        else:
          nums.pop()
  else: 
    if is_reverse == True:
      nums.reverse()
    print('[' + ','.join(str(num) for num in nums) +']')
