import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    q = [[0]*3 for _ in range(N)]

    # 90
    for j in range(N):
        st = ''
        for i in range(N-1, -1,-1):
            st += arr[i][j]
        q[j][0] = st

    # 180
    for i in range(N-1, -1, -1):
        st = ''
        for j in range(N-1, -1, -1):
            st += arr[i][j]
        q[N-1-i][1] = st

    # 270
    for j in range(N-1, -1,-1):
        st = ''
        for i in range(N):
            st += arr[i][j]
        q[N-1-j][2] = st

    print(f'#{tc}')
    for ans in q:
        print(*ans)