import sys
sys.stdin = open("input.txt", "r")


def sol():
    q = []
    q.append((0, 0))        # 0초, 0개
    while lst:
        sec, cnt = q.pop(0)     # sec: 초, cnt: 초당 빵갯수
        sec += 1
        if sec % M == 0:
            cnt += K

        while lst.pop(0) == sec:    # 손님이 온 시간
            if not cnt:             # 붕어빵 없으면 못줌
                return 'Impossible'
            else:                   # 붕어빵 있으면 주기
                cnt -= 1

        q.append((sec, cnt))

    return 'Possible'


t = int(input())
for tc in range(1, 1+t):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    if lst[0] < M:
        ans = 'Impossible'
        print(f'#{tc} {ans}')
    else:
        ans = sol()
        print(f'#{tc} {ans}')
