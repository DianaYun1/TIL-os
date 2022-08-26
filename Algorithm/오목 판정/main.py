import sys
sys.stdin = open("sample_input.txt", "r")


def bfs(si, sj):
    d = [(0, 1), (1, 0), (1, 1), (1, -1)]
    mx = []
    for di, dj in d:
        cnt = 1
        ni, nj = si + di, sj + dj
        while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
            cnt += 1
            ni, nj = ni + di, nj + dj
        mx.append(cnt)

    return mx


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if max(bfs(i, j)) >= 5:
                    ans = 'YES'
                    break

    print(f'#{tc} {ans}')