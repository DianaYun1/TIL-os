import sys
sys.stdin = open("s_input.txt", "r")


def dfs(si, sj):
    visited[si][sj] = 1
    q = []
    q.append((si, sj, 0))

    while q:
        i, j, d = q.pop(0)
        if i == ei and j == ej:
            return d-1       # 도착지 포함 안하니까 1 빼줌

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != '1':
                visited[ni][nj] = 1
                q.append((ni, nj, d+1))
    return 0


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    visited = [[0]*N for _ in range(N)]
    ans = dfs(si, sj)

    print(f'#{tc} {ans}')