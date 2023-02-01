import sys
sys.stdin = open("s_input.txt", "r")

pri = {'+': 1, '*': 2}
# T = 10
T = int(input())
for test_case in range(1, T + 1):
    # _ = input()
    st = input()

    equ = ''
    stk = []
    # [1] 중위표기식 -> 후위표기식
    for ch in st:
        if ch.isdigit():  # 숫자인 경우: equ에 추가
            equ += ch
        else:  # 연산자인 경우
            while stk and pri[ch] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)

    # [1] 남은 연산자를 순서대로 pop, equ에 추가
    while stk:
        equ += stk.pop()

    print(f'#{test_case} {equ}')