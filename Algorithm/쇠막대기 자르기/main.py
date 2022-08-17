import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    lst = input()
    laser = '()'
    cnt = stick = ans = 0
    s = []

    i = 0
    while i < len(lst):
        if lst[i:i+2] == laser:
            cnt += stick
            i += 2
        elif lst[i] == '(':
            stick += 1
            i += 1
        elif lst[i] == ')':
            cnt += 1
            stick -= 1
            i += 1

    print(f'#{tc} {cnt}')