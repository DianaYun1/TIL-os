import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mx = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            ans = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    ans += arr[x][y]
                    if mx < ans:
                        mx = ans

    print(f'#{tc} {mx}')
