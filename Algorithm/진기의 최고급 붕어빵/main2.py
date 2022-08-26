import sys
sys.stdin = open("input.txt", "r")


t = int(input())
for tc in range(1, 1+t):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 'Possible'

    if lst[0] < M:
        ans = 'Impossible'
    else:
        for i in range(N):
            if lst[i]//M * K < i+1:
                ans = 'Impossible'
                break

    print(f'#{tc} {ans}')
