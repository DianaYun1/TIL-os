w, h = map(int, input().split())
n = int(input())
arr = []
for i in range(n+1):
    d, l = map(int, input().split())
    if d == 1:      # 북
        arr.append((l, h))
    elif d == 2:    # 남
        arr.append((l, 0))
    elif d == 3:    # 서
        arr.append((0, h-l))
    elif d == 4:    # 동
        arr.append((w, h-l))

x, y = arr.pop()
ans = []
print(arr, x, y)
for a, b in arr:
    if x == a:
        s = min(x, w-x)*2 + h
    elif x != a:
        if y == b:
            s = abs(x-a)
        else:
            s = min(x+a, w-x+w-a) + h

    elif y == b:
        s = min(y, h-y)*2 + w
    elif y != b:
        if x == a:
            s = abs(y - b)
        else:
            s = min(y + b, h - y + h - b) + w

    else:
        s = abs(x-a) + abs(y-b)

    ans.append(s)
print(ans)
print(sum(ans))