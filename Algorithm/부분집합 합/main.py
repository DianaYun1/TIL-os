import sys
sys.stdin = open("s_in2.txt", "r")

T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    ans = 0
    k = 0
    N = len(lst)  # N bit (lst member: N)

    for bit in range(1, 2 ** N):  # == 1<<N
        sm = 0
        for i in range(0, N):  # every lst index
            if (bit >> i) & 1:
                sm += lst[i]
        if sm == k:
            ans = 1
            break

    # plus = []
    # minus = []
    # for i in range(len(lst)):
    #     if lst[i] > 0:
    #         plus.append(lst[i])
    #     elif lst[i] < 0:
    #         minus.append(lst[i])
    # else:
    #     ans = 1
    #     # for i in range()


    print(f'#{tc} {ans}')
