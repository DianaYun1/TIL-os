import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # sol-1
    # num = input()
    # mx = 0
    # mx_number = '0'
    # for number in num:
    #     cnt = 0
    #     for i in range(n):
    #         if number == num[i]:
    #             cnt += 1
    #     if mx <= cnt:
    #         mx = cnt
    #         if mx_number < number:
    #             mx_number = number
    # print(f'#{tc} {mx_number} {mx}')

    #sol-2
    lst = list(map(int, input()))
    cnts = [0]*10
    for n in lst:
        cnts[n] += 1

    idx = 0
    for i in range(1, 10):
        if cnts[idx] <= cnts[i]:
            idx = i

    print(f'#{tc} {idx} {cnts[idx]}')