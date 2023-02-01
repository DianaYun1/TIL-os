import sys
sys.stdin = open("s_input.txt", "r")


def dfs(n, sm):
    global ans

    if ans <= sm:
        return

    if n == N:
        if ans > sm:
            ans = sm
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, sm+arr[n][j])
            visited[j] = 0


t = int(input())
for tc in range(1, 1+t):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 10*N
    visited = [0]*N
    dfs(0, 0)       # n = 0, sm = 0

    print(f'#{tc} {ans}')