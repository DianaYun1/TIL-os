k = int(input())
w = h = 0
d = []
l = []
for _ in range(6):
    di, le = map(int, input().split())
    d.append(di)
    l.append(le)
    if di == 1 or di == 2:
        w = max(w, le)
    else:
        h = max(h, le)

s = w*h

if d.count(2) == 1 and d.count(4) == 1:
    for i in range(6):
        if d[i] == 1 and d[(i-1)%6] == 3 and d[(i+1)%6] == 3:
            s -= l[i] * l[(i+1)%6]

elif d.count(1) == 1 and d.count(4) == 1:
    for i in range(6):
        if d[i] == 3 and d[(i-1)%6] == 2 and d[(i+1)%6] == 2:
            s -= l[i] * l[(i+1)%6]

elif d.count(1) == 1 and d.count(3) == 1:
    for i in range(6):
        if d[i] == 2 and d[(i-1)%6] == 4 and d[(i+1)%6] == 4:
            s -= l[i] * l[(i+1)%6]

elif d.count(2) == 1 and d.count(3) == 1:
    for i in range(6):
        if d[i] == 4 and d[(i-1)%6] == 1 and d[(i+1)%6] == 1:
            s -= l[i] * l[(i+1)%6]

print(s*k)