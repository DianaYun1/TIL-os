import sys
sys.stdin = open("s_input.txt", "r")


def dfs(si, sj):
    stk = []
    visited[si][sj] = 1

    while True:
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si+di, sj+dj
            # 숫자가 2, 3으로 주어졌으니 길이면 가라가 아님! 길이 아니면 가라!!
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] != '1':
                stk.append((si, sj))

                si, sj = ni, nj
                visited[ni][nj] = 1
                break

        else:
            if stk:
                si, sj = stk.pop()
            else:
                break


t = int(input())
for tc in range(1, 1+t):
    n = int(input())
    arr = [input() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    visited = [[0]*n for _ in range(n)]
    dfs(si, sj)

    print(f'#{tc} {visited[ei][ej]}')