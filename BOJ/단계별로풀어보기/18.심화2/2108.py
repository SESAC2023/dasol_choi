#통계

import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(int(input()) for _ in range(n)))

def find_mode(nums):
    cnt_dict = {}
    max_cnt = 0
    modes = []
    
    # 각 숫자의 빈도수 계산
    for num in nums:
        if num in cnt_dict:
            cnt_dict[num] += 1
        else:
            cnt_dict[num] = 1
        max_cnt = max(max_cnt, cnt_dict[num])
    
    # 최빈값 찾기
    for num, count in cnt_dict.items():
        if count == max_cnt:
            modes.append(num)
    
    # 최빈값 중 두 번째로 작은 값 찾기
    if len(modes) == 1:
      second_smallest_mode = modes[0]
    else:
      second_smallest_mode = modes[1]
    
    return second_smallest_mode


s = int(round(sum(nums) / n, 0))
print(s)  #산술평균
print(nums[int((n) / 2)])  #중앙값
print(find_mode(nums))
print(nums[-1] - nums[0])  #범위
