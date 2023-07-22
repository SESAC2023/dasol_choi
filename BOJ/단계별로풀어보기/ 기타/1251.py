# 단어 나누기

word = input().strip()
n = len(word)

# index 기준으로 문자열 재배치
def rearrange(word, a, b):
  s_1, s_2, s_3 = word[0:a][::-1], word[a:b][::-1], word[b:][::-1]
  res = s_1 + s_2 + s_3
  return res

# 중복없이 2개 index 뽑기
def dfs(start):
    if len(stack)==2:
        new_word = rearrange(word, stack[0], stack[1])
        new_words.append(new_word)
        return   
    for i in range(start, n):
        if i not in stack:
            stack.append(i)
            dfs(i+1)
            stack.pop()         

stack = []
visited = [False] * (n)
new_words = []

dfs(1)

print(sorted(new_words)[0])
