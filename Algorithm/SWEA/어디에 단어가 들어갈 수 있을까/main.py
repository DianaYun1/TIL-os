import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):  # 가로 탐색
        cnt = 0
        j = 0
        while j < n:
            if arr[i][j] == 1:
                cnt += 1
            if (arr[i][j] == 0 or j == n-1) and cnt != 0:
                if cnt == k:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
            j += 1

    for i in range(n):  # 세로 탐색
        cnt = 0
        j = 0
        while j < n:
            if arr[j][i] == 1:
                cnt += 1
            if (arr[j][i] == 0 or j == n-1) and cnt != 0:
                if cnt == k:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
            j += 1

    print(f'#{tc} {ans}')
