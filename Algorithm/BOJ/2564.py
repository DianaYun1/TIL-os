w, h = map(int, input().split())
n = int(input())
arr = []
for _ in range(n+1):
    a, b = map(int, input().split())
    if a in [1, 2]:
        arr.append((a, b))
    else:
        arr.append((a, h-b))
x, y = arr.pop()

s = 0
for i in range(n):
    a, b = arr[i]
    if x == a:
        s += abs(y-b)
    elif x in [1, 2]:
        if a in [1, 2]:
            s += h + min(y, w-y, b, w-b)*2 + abs(y-b)
        elif a == 3:
            if x == 1:
                s += y+h-b
            else:
                s += y+b
        elif a == 4:
            if x == 1:
                s += w-y + h - b
            else:
                s += w-y + b
    else:
        if a in [3, 4]:
            s += w + min(y, h-y, b, h-b)*2 + abs(y-b)
        elif a == 1:
            if x == 3:
                s += h-y+b
            else:
                s += h-y+w-b
        elif a == 2:
            if x == 3:
                s += y + b
            else:
                s += y + w-b

print(s)


# for i in range(n+1):
#     d, l = map(int, input().split())
#     if d == 1:      # 북
#         arr.append((l, h))
#     elif d == 2:    # 남
#         arr.append((l, 0))
#     elif d == 3:    # 서
#         arr.append((0, h-l))
#     elif d == 4:    # 동
#         arr.append((w, h-l))
#
# x, y = arr.pop()
# ans = []
#
# for a, b in arr:
#     if x == a and y == b:
#         s = 0
#     elif x == a:
#         if y+b == h:
#             s = min(x, w-x)*2 + h
#         else:
#             s = abs(y - b)
#
#     elif y == b:
#         if x + a == w:
#             s = min(y, h - y) * 2 + w
#         else:
#             s = abs(x - a)
#     else:
#         if y+b == h:
#             s = min(x+a, w-x+w-a) + h
#
#         elif x+a == w:
#             s = min(y + b, h - y + h - b) + w
#
#         else:
#             s = abs(x-a) + abs(y-b)
#
#     ans.append(s)
#
# print(sum(ans))
