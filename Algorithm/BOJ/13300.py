n, k = map(int, input().split())
# male = [0]*6
# female = [0]*6
arr = [[0]*6 for _ in range(2)]
cnt = 0

for _ in range(n):
    s, y = map(int, input().split())
    arr[s][y-1] += 1
    if arr[s][y-1] % k == 0:
        arr[s][y - 1] = 0
        cnt += 1
    # if s:   # 남
    #     male[y-1] += 1
    #     if male[y-1] % k == 0:
    #         male[y-1] = 0
    #         cnt += 1
    #
    # else:   # 여
    #     female[y-1] += 1
    #     if female[y-1] % k == 0:
    #         female[y-1] = 0
    #         cnt += 1

for i in range(2):
    for j in range(6):
        if arr[i][j]:
            cnt += 1
    # if male[i]:
    #     cnt += 1
    # if female[i]:
    #     cnt += 1

print(cnt)

