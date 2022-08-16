import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    lst = input()
    laser = '()'
    cnt = 0

    for i in range(len(lst)-1):
        if lst[i:i+2] == laser:
            cnt += 1
    print(cnt)

    # print(f'#{tc} {ans}')