arr = [list(map(int, input().split())) for _ in range(5)]
nums = []
# bing = 0   # 빙고 갯수


def bingo():
    arr2 = list(zip(*arr))
    bing = 0    # 빙고 갯수
    r = []
    l = []
    for i in range(5):  # 행
        if arr[i].count(0) == 5:
            bing += 1
    for j in range(5):  # 열
        if arr2[j].count(0) == 5:
            bing += 1
    for k in range(5):  # 대각선
        r.append(arr[k][k])
        l.append(arr[k][5-k-1])
    if r.count(0) == 5:
        bing += 1
    if l.count(0) == 5:
        bing += 1

    return bing


for _ in range(5):
    k = list(map(int, input().split()))
    for i in range(5):
        nums.append(k[i])

'''
for n in range(25):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == nums[n]:
                arr[i][j] = 0
                if bingo() >= 3:
                    print(n+1)
                    exit()
'''

# '''
for n in range(25):
    if n >= 12 and bingo() >= 3:
        print(n)
        break
    for i in range(5):
        for j in range(5):
            if arr[i][j] == nums[n]:
                arr[i][j] = 0

# '''