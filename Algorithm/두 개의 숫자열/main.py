import sys
sys.stdin = open("input.txt", "r")


def cal(short, long, n, m):
    mx = 0
    i = 0
    while i <= m-n:
        sm = 0
        for j in range(i, i+n):
            sm += short[j-i] * long[j]
        if mx < sm:
            mx = sm
        i += 1
    return mx


t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0

    if N == M:
        for i in range(N):
            ans += A[i] * B[i]
    elif N < M:
        ans = cal(A, B, N, M)
    else:
        ans = cal(B, A, M, N)

    print(f'#{tc} {ans}')