import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    pn = [2, 3, 5, 7, 11]
    lst = [0]*len(pn)

    for i in range(len(pn)):
        while n % pn[i] == 0:
            n //= pn[i]
            lst[i] += 1

    print(f'#{tc}', *lst)