import sys
sys.stdin = open("input.txt", "r")

t = 10
for tc in range(1, t+1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    mn = 100**2
    lst = []

    for y in range(100):
        if arr[0][y] == 1:
            lst.append(y)

    for y in lst:
        cnt = 1
        stk = []
        i, j = 0, y
        while i < 99:
            stk.append((i, j))
            if 0 < j < 100 and arr[i][j-1] == 1 and (i, j-1) not in stk:
                cnt += 1
                j -= 1
            elif 0 <= j < 99 and arr[i][j+1] == 1 and (i, j+1) not in stk:
                cnt += 1
                j += 1
            elif arr[i+1][j] == 1 and (i+1, j) not in stk:
                cnt += 1
                i += 1
        if mn >= cnt:
            mn = cnt
            ans = y

    print(f'#{tc} {ans}')
