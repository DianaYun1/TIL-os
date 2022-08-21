import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):  # 너비
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > ans:
                    ans = cnt
            else:
                cnt = 0

    for j in range(m):  # 깊이
        cnt = 0
        for i in range(n):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > ans:
                    ans = cnt
            else:
                cnt = 0

    print(f'#{tc} {ans}')
