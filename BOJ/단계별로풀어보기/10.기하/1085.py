#직사각형에서 탈출

x, y, w, h = map(int, input().split())

xw_gap = w-x
yh_gap = h-y

print(min(xw_gap, yh_gap, x, y))
