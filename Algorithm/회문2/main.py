import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    n = 100
    arr = list(input() for _ in range(n))
    arr_T = list(zip(*arr))
    ans = 1
    for m in range(2, 100):
        for i in range(n):
            for j in range(n-m+1):
                if arr[i][j:j + m // 2] == arr[i][j+m-1:j + (m+1) // 2 - 1:-1]:
                    if ans < m:
                        ans = m

    for m in range(2, 100):
        for i in range(n):
            for j in range(n-m+1):
                if arr_T[i][j:j + m // 2] == arr_T[i][j+m-1:j + (m+1) // 2 - 1:-1]:
                    if ans < m:
                        ans = m

    print(f'#{tc} {ans}')
