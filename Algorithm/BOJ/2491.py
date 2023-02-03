n = int(input())
lst = list(map(int, input().split()))
up = down = ans = 1

for i in range(n-1):
    if lst[i] == lst[i+1]:
        up += 1
        down += 1
    elif lst[i] < lst[i+1]:
        if down != 1:
            down = 1
        up += 1
    elif lst[i] > lst[i + 1]:
        if up != 1:
            up = 1
        down += 1

    ans = max(up, down, ans)

print(ans)
