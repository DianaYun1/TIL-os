import sys
sys.stdin = open("s_input.txt", "r")


def bfs(si, sj):
    q = []
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if ci == ei and cj == ej:
            return 1

        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0


t = int(input())
for tc in range(1, 1+t):
    N = int(input())
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    visited = [[0]*N for _ in range(N)]
    bfs(si, sj)

    print(f'#{tc} {visited[ei][ej]}')