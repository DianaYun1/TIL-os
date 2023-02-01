import sys
sys.stdin = open("s_input.txt", "r")


def solve(s, e):
    # 종료 조건
    if s == e:
        return s

    # 하부 호출, 단위 작업: 2등분해서 각각 승자 -> 최종 승자
    a = solve(s, (s+e)//2)
    b = solve((s+e)//2+1, e)

    if (lst[a] % 3)+1 == lst[b]:   # b가 이긴 경우
        return b
    else:       # 비기거나 a가 이긴 경우
        return a


t = int(input())
for tc in range(1, 1+t):
    n = int(input())
    lst = [0] + list(map(int, input().split()))

    ans = solve(1, n)

    print(f'#{tc} {ans}')
