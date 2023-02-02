n = int(input())
rec = [[0]*101 for _ in range(101)]
ans = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            rec[j][i] = 1

for i in range(101):
    ans += sum(rec[i])

print(ans)


