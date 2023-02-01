import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = input()
    top = -1

    for i in lst:
        if i == '(':
            top += 1
        elif i == ')':
            top -= 1

    if top == -1:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')