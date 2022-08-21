import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    cntA = cntB = 0

    l, r, c = 1, p, 0
    while c != a:
        c = int((l+r)/2)
        if c < a:
            l = c
        else:
            r = c
        cntA += 1

    l, r, c = 1, p, 0
    while c != b:
        c = int((l+r)/2)
        if c < b:
            l = c
        else:
            r = c
        cntB += 1

    if cntA > cntB:
        ans = 'B'
    elif cntA < cntB:
        ans = 'A'
    else:
        ans = 0

    print(f'#{tc} {ans}')