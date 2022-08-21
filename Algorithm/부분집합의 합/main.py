import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())


for tc in range(1, T+1):
    n, k = map(int, input().split())
    lst = list(range(1, 13))
    ans = 0

    for bit in range(1, 1 << 12):  # == 1<<N 자릿수 지우
        sm = cnt = 0
        for i in range(12):  # every lst index
            if (bit >> i) & 1:
                sm += lst[i]
                cnt += 1
        if sm == k and cnt == n:
            ans += 1

    print(f'#{tc} {ans}')