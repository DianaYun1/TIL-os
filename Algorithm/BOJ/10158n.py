w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dx = dy = 1

for i in range(t):
    p, q = p+dx, q+dy
    if (p, q) in [(w, h), (0, 0), (0, h), (w, 0)]:
        dx *= -1
        dy *= -1
    elif (p == w or p == 0) and 0 < q < h:
        dx *= -1
    elif (q == h or q == 0) and 0 < p < w:
        dy *= -1

print(p, q)