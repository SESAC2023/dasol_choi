#숫자 카드

n = int(input())
n_list = list( map(int, input().split()))
n_dict = {}
for x in n_list:
  n_dict[x] = 1

m = int(input())
m_list = list(map(int, input().split()))

for x in m_list:
  try:
    print(n_dict[x], end=" ")
  except:
    print(0, end=" ")
