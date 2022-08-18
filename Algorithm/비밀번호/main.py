import sys
sys.stdin = open("s_input.txt", "r")


t = 10
for tc in range(1, t+1):
    n, st = input().split()
    n = int(n)
    stk = []
    pw = ''

    for s in st:
        if stk and s == stk[-1]:
            stk.pop()
        else:
            stk.append(s)

    print(f'#{tc} ', *stk, sep='')