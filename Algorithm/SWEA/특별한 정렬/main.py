import sys
sys.stdin = open("s_input.txt", "r")

def max_min(lst):
    mx, mn = 1, 100
    for i in range(len(lst)):
        if len(lst) == 0:
            break
        if lst[i] < mn:
            mn = lst[i]
            # i_min = i
        if lst[i] < mx:
            mx = lst[i]
            # i_max = i

    lst.remove(mx)
    lst.remove(mn)
    return mx, mn



T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = max_min(lst)

    print(f'#{tc} {ans}')