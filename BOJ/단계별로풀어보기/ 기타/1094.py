# 막대기

x = int(input())

sticks = [64]

while True:
  if sum(sticks) > x:
    min_stick = sticks.pop() 
    split_stick = min_stick/2
    sticks.append(split_stick)
    if sum(sticks) < x:
      sticks.append(split_stick)
  else : break
print(len(sticks))
