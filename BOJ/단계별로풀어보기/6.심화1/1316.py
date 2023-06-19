#그룹 단어 체커

# 입력받은 단어가 그룹 단어이면 1, 아니면 0을 반환하는 함수 
def check_group_word(word):
  letters = []
  for letter in word:
    if letter not in letters:
      letters.append(letter)
    else:
      # 중복문자가 존재하는 경우, 연속해서 등장하지 않는다면 바로 탈락!
      if letters[-1] != letter:
        res = 0
        break
    res = 1
  return res

n = int(input())
cnt = 0
for i in range(n):
  word = input()
  score = check_group_word(word)
  cnt += score  #그룹단어의 수 더하기
print(cnt) 
