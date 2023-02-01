import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())//10

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    # 이전 경우 그대로, 전전 경우 *2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]*2

    print(f'#{tc} {dp[n]}')