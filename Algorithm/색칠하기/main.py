import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 색 겹칠때 코드
                # if arr[i][j] == 0:
                #     arr[i][j] = color
                # elif arr[i][j] == 2 and color == 1:
                #     arr[i][j] += color
                # elif arr[i][j] == 1 and color == 2:
                #     arr[i][j] += color

                arr[i][j] += color

                if arr[i][j] == 3:  # 보라색이면 cnt+1하고 배열 -1로 바꾸기
                    cnt += 1
                    # arr[i][j] = -1

    # cnt = 0
    # for i in range(10):
    #     for j in range(10):
    #         if arr[i][j] == 3:
    #             cnt += 1

    print(f'#{tc} {cnt}')