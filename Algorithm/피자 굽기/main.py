import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = []

    for i in range(N):
        q.append((i+1, lst[i]))

    i = N
    while q:
        ans, chi = q.pop(0)
        chi //= 2
        if chi == 0:
            if i < M:
                q.append((i+1, lst[i]))
                i += 1
        else:
            q.append((ans, chi))

    print(f'#{tc} {ans}')