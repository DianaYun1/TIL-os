import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    i = n-1
    sell = lst[i]
    while i >= 0:
        if sell <= lst[i]:
            sell = lst[i]
        else:
            ans += sell - lst[i]
        i -= 1

    print(f'#{tc} {ans}')