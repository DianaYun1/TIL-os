import sys
sys.stdin = open("s_input.txt", "r")

pri = {'+':1, '*':2}
t = int(input())
for tc in range(1, 1+t):
    st = input()

    eq = ''
    stk = []

    for ch in st:
        if ch.isdigit():
            eq += ch
        else:
            if not stk:
                stk.append(ch)
            else:
                if pri[ch] > pri[stk[-1]]:
                    stk.append(ch)
                else:
                    while stk and pri[ch] <= pri[stk[-1]]:
                        eq += stk.pop()
                    stk.append(ch)

    while stk:
        eq += stk.pop()

    print(f'#{tc} {eq}')