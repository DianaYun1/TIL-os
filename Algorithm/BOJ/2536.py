m, n = map(int, input().split())
k = int(input())
bus = []
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    bus.append((b, x1, y1, x2, y2))
sx, sy, dx, dy = map(int, input().split())

for b, x1, y1, x2, y2 in bus:
    if x1 == x2:

        pass
    elif y1 == y2:
        pass