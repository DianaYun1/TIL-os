import sys
sys.stdin = open("s_input.txt", "r")


def dfs(n, sm):
    global ans

    # 가지치기는 제일 위에서, 제일 마지막 순서로 작성
    if sm > K:
        return

    # 종료조건
    if n == N:
        if sm == K:
            ans += 1
        return

    # dfs(n+1) 호출
    dfs(n+1, sm+lst[n])     # 사용하는 경우
    dfs(n+1, sm)            # 사용하지 않는 경우


t = int(input())
for tc in range(1, 1+t):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)

    print(f'#{tc} {ans}')