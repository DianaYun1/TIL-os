import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*i for i in range(1, n+1)]
    for i in range(n):
        arr[i][0] = arr[i][-1] = 1
    print(arr)


    # print(f'#{tc}', *ans)