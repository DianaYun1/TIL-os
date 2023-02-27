n = int(input())
arr = [[0]*1002 for _ in range(1002)]
lst = []
ans = [0]*n
for _ in range(n):
    x, y, w, h = map(int, input().split())
    lst.append((x, y, w, h))

for k in range(n):
    x, y, w, h = lst[n-k-1]
    for i in range(w):
        for j in range(h):
            if not arr[x + i][y + j]:
                arr[x + i][y + j] = 1
                ans[n-k-1] += 1

for s in ans:
    print(s)