import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    cnt = 1
    i = j = d = 0
    arr[0][0] = 1
    while cnt <= n*n:
        ni, nj = i + di[d], j + dj[d]
        if arr[ni][nj] == 0 and 0 <= ni < n and 0 <= nj < n:
            pass

        else:
            d = (d + 1) % 4
            ni, nj = i + di[d], j + dj[d]

        i, j = ni, nj
        arr[i][j] = cnt
        cnt += 1

    print(f'#{tc} {arr}')
