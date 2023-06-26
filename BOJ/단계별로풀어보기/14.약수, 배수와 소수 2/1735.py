#분수 합

import sys
input = sys.stdin.readline

a1, a2 = map(int, input().strip().split())
b1, b2 = map(int, input().strip().split())

new1 = a1*b2+b1*a2
new2 = a2*b2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd = gcd(new1, new2)
print(int(new1/gcd), int(new2/gcd))
