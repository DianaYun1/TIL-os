import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    # sol-1 다 더함
    # mx = 0
    # mn = 10000*m

    # for i in range(n-m+1):
    #     s = 0
    #     for j in range(i, i+m):
    #         s += lst[j]
    #     if s > mx:
    #         mx = s
    #     if s < mn:
    #         mn = s
    # ans = mx - mn

    # sol-2 추가되는거 더하고 앞에거 뺌
    s = 0
    for i in range(m):
        s += lst[i]
    mn = mx = s

    for i in range(m, n):
        s = s + lst[i] - lst[i-m]
        if mx < s : mx = s
        if mn > s : mn = s
    ans = mx - mn

    # sol-3
    # s = []
    # for i in range(n-m+1):
    #     s.append(sum(lst[i:i+m]))
    # ans = max(s) - min(s)

    print(f'#{tc} {ans}')