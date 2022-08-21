import sys
sys.stdin = open("s_list2.txt", "r")

T = int(input())
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                ans += ni + nj

    print(f'#{tc} {ans}')
