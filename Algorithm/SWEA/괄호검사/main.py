import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    st = input()
    stk = []
    ans = 0

    for s in st:
        if s == '(' or s == '{':
            stk.append(s)
        if s == ')' or s == '}':
            if len(stk) == 0:   # if not stk:
                stk.append(s)
                break
            elif (s == ')' and stk[-1] != '(') or (s == '}' and stk[-1] != '{'):
                stk.append(s)
                break
            else:
                stk.pop()

    if len(stk) == 0:
        ans = 1

    print(f'#{tc} {ans}')
