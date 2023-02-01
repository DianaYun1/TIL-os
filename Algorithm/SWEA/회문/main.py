import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(input() for _ in range(n))
    ans = ''

    for i in range(n):
        for j in range(n-m+1):
            if arr[i][j:j + m // 2] == arr[i][j+m-1:j + (m+1) // 2 - 1:-1]:
                ans = arr[i][j:j + m]
                break
    arr_T = list(zip(*arr))

    for i in range(n):
        for j in range(n-m+1):
            if arr_T[i][j:j + m // 2] == arr_T[i][j+m-1:j + (m+1) // 2 - 1:-1]:
                ans = arr_T[i][j:j + m]
                break

    print(f'#{tc} ', *ans, sep='')
