import sys
sys.stdin = open("input.txt", "r")


def dfs():
    visited[si][sj] = 1
    q = []
    q.append((si, sj))

    while q:
        i, j = q.pop()
        if i == ei and j == ej:
            visited[ei][ej] = 1
            break

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != '1':
                visited[ni][nj] = 1
                q.append((ni, nj))


t = 10
for tc in range(1, t+1):
    _ = int(input())
    N = 16
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    visited = [[0]*N for _ in range(N)]
    dfs()

    print(f'#{tc} {visited[ei][ej]}')