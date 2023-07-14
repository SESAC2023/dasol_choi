# 괄호

import sys
ip = sys.stdin.readline

t = int(ip())
for _ in range(t):
    stack = []
    a =ip().rstrip()
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        print('NO') if stack else print('YES')
