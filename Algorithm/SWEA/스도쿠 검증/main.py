import sys
sys.stdin = open("s_input.txt", "r")


t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    # 가로
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            num = arr[i][j]
            check[num] += 1
            if check[num] == 2:
                ans = 0
                break

    # 세로
    for j in range(9):
        check = [0] * 10
        for i in range(9):
            num = arr[i][j]
            check[num] += 1
            if check[num] == 2:
                ans = 0
                break
    # 3*3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0] * 10
            for x in range(i, i+3):
                for y in range(j, j+3):
                    num = arr[x][y]
                    check[num] += 1
                    if check[num] == 2:
                        ans = 0
                        break

    print(f'#{tc} {ans}')