import sys
sys.stdin = open("input.txt", "r")


t = 10
for tc in range(1, t+1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100**2

    for sj in range(1, 101):
        if arr[0][sj] == 0:
            continue

        cj = sj
        ci = cnt = direction = 0
        while ci < 99:
            cnt += 1
            if direction == 0:  # 아래방향
                ci += 1
                if arr[ci][cj-1] == 1:
                    direction = -1      # 왼쪽
                elif arr[ci][cj+1] == 1:
                    direction = 1       # 오른쪽
            else:
                cj += direction
                if arr[ci][cj+direction] == 0:
                    direction = 0

        if mn >= cnt:
            mn, ans = cnt, sj-1

    print(f'#{tc} {ans}')
