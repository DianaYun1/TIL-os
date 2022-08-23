import sys
sys.stdin = open("input.txt", "r")

pri = {'+':1, '*':2}
t = 10
for tc in range(1, 1+t):
    n = int(input())
    st = input()

    eq = ''
    stk = []

    # 후위표기식
    for ch in st:
        if ch.isdigit():
            eq += ch
        else:
            while stk and pri[ch] <= pri[stk[-1]]:
                eq += stk.pop()
            stk.append(ch)

    while stk:
        eq += stk.pop()

    # 후위표기식 계산
    for ch in eq:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if ch == '+':
                stk.append(op1+op2)
            else:
                stk.append(op1*op2)

    print(f'#{tc} {stk.pop()}')
