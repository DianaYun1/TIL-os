import sys
sys.stdin = open("s_input.txt", "r")




t = int(input())
for tc in range(1, 1+t):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    g1 = []
    g2 = []
    for i in range((1+n)//2+1):
        g1.append(lst[i])

    for i in range((1+n)//2+1, n):
        g2.append(lst[i])

    i = 0
    stk = []
    while i < len(g1):
        if i+1 < len(g1):
            k = g1[i]-g1[i+1]
            if k == 1 or k == -2 or k == 0:
                stk.append(g1[i])
            elif k == -1 or k == 2:
                stk.append(g1[i + 1])
        else:
            stk.append(g1[i])

        i += 2



    print(f'#{tc} {ans}')