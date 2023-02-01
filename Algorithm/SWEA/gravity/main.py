import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(f'#{test_case} {ans}')