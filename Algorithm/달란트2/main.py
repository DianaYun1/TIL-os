import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, 1 + t):
    N, P = map(int, input().split())
    ans = 0
    group = N // P  # 기본 묶음
    plus = N % P    # 하나씩 더해줘야하는 묶음 수

    if plus:
        ans = (group+1)**plus * group**(P-plus)
    else:
        ans = group**P

    print(f'#{tc} {ans}')