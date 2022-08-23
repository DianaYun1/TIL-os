import sys
sys.stdin = open("s_input.txt", "r")


t = int(input())
for tc in range(1, 1+t):
    st = input().split()
    stk = []

    for ch in st:
        if ch.isdigit():
            stk.append(int(ch))
        elif ch == '.':
            ans = stk.pop()
            break
        else:
            if len(stk) < 2:
                ans = 'error'
                break
            num2 = stk.pop()
            num1 = stk.pop()
            if ch == '+':
                stk.append(num1+num2)
            elif ch == '-':
                stk.append(num1-num2)
            elif ch == '*':
                stk.append(num1*num2)
            elif ch == '/':
                stk.append(num1/num2)
            else:
                ans = 'error'
                break

    if stk:
        ans = 'error'

    print(f'#{tc} {ans}')