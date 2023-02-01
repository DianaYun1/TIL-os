import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    arr = list(input() for _ in range(5))
    ans = ''
    for j in range(15):
        for i in range(5):
            try:
                ans += arr[i][j]
            except:
                pass
    print(f'#{tc} {ans}')
