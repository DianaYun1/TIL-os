import sys
sys.stdin = open("s_in.txt", "r")

def bin_search(lst, s, e, d):
    while s <= e:
        m = (s+e)//2
        if lst[m] == d:
            return m+1
        elif lst[m] > d:
            e = m - 1
        else:
            s = m + 1
    return 0

T = int(input())

for tc in range(1, T+1):
    N, D = map(int,input().split())
    lst = list(map(int, input().split()))

    ans = bin_search(lst, 0, N-1, D)

    print(f'#{tc} {ans}')