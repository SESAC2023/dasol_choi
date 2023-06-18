#A+B - 4

import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    a, b = map(int, line.split())    
    print(a+b)
