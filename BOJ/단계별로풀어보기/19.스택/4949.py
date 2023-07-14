# 균형잡힌 세상

import sys
input = sys.stdin.readline

def is_balanced(string):
    stack = []
    opening = "(["
    closing = ")]"
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return "no"
            elif opening.index(stack[-1]) == closing.index(char):
                stack.pop()
            else:
                return "no"
    if len(stack) == 0:
        return "yes"
    else:
        return "no"

while True:
    string = input().rstrip()
    if string == ".":
        break
    else:
        result = is_balanced(string)
        print(result)
