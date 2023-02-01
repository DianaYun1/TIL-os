import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    equ = input().split()
    stk = []

    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            try:
                if ch == '.':
                    ans = stk.pop()
                else:
                    op2 = stk.pop()
                    op1 = stk.pop()
                    if ch == '+':
                        stk.append(op1 + op2)
                    elif ch == '-':
                        stk.append(op1 - op2)
                    elif ch == '*':
                        stk.append(op1 * op2)
                    elif ch == '/':
                        stk.append(op1 // op2)
                    else:
                        ans = 'error'
                        break
            except:
                ans = 'error'
                break
    if stk:
        ans = 'error'

    print(f'#{test_case} {ans}')