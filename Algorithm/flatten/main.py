import sys
sys.stdin = open("s_input.txt", "r")

for tc in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    for i in range(n):
        if lst[-1] - lst[0] <= 1:
            break
        lst[0] += 1
        lst[-1] -= 1
        lst.sort()

    height = lst[-1] - lst[0]

    print(f'#{tc} {height}')