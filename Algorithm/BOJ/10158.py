w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
direc = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
d = direc[0]

for i in range(t):
    p, q = p+d[0], q+d[1]
    if (p, q) == (w, h):
        d = direc[2]
    elif (p, q) == (0, 0):
        d = direc[0]
    elif p == w:
        if d == direc[0]:
            d = direc[1]
        elif d == direc[3]:
            d = direc[2]
    elif q == h:
        if d == direc[1]:
            d = direc[2]
        elif d == direc[0]:
            d = direc[3]
    elif p == 0:
        if d == direc[2]:
            d = direc[3]
        elif d == direc[1]:
            d = direc[0]
    elif q == 0:
        if d == direc[3]:
            d = direc[0]
        elif d == direc[2]:
            d = direc[1]
print(p, q)