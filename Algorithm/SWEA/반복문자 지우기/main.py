import sys

sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t + 1):
    st = input()
    stk = []

    for s in st:
        if not stk:
            stk.append(s)
        elif stk[-1] == s:
            stk.pop()
        else:
            stk.append(s)

    print(f'#{tc} {len(stk)}')