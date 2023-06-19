#너의 평점은

score_table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total_sub_score = 0  #학점의 총합
temp = 0  #(학점x과목평점)

for _ in range(20):
  name, sub_score, get_score = input().split(' ')
  if get_score != 'P':
    get_score = score_table[get_score]  #등급을 과목평점으로 변경(score_table 참조)
    total_sub_score += float(sub_score)  # 학점의 총합 더하기
    temp += (float(sub_score) * get_score)  #(학점x과목평점)의 합 더하기

print(temp/total_sub_score)  #(학점x과목평점)의 합 / 학점의 총합
