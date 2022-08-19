import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    center = n//2
    arr = [list(input()) for _ in range(n)]
    lst = list(range(center)) + list(range(center, -1, -1))
    ans = 0

    for i in range(n):
        for j in range(center-lst[i], center+lst[i]+1):
            ans += int(arr[i][j])

    print(f'#{tc} {ans}')