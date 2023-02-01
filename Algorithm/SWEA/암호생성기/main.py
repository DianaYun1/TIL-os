import sys
sys.stdin = open("input.txt", "r")

t = 8
for tc in range(1, 1+t):
    _ = input()
    lst = list(map(int, input().split()))
    q = lst

    i, j = 1, 0
    while True:
        num = q[j] - i
        if num <= 0:
            num = 0
            q.append(num)
            break
        q.append(num)

        i += 1
        j += 1
        if i == 6:
            i = 1

    print(f'#{tc}', *q[-8:])