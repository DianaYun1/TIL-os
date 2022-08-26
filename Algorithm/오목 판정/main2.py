import sys
sys.stdin = open("sample_input.txt", "r")


def sol():
    d = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in range(N):
        for j in range(N):
            for di, dj in d:
                for mul in range(5):
                    ni, nj = i + di*mul, j + dj*mul
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        continue
                    break

                else:
                    return 'YES'
    return 'NO'


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = sol()

    print(f'#{tc} {ans}')