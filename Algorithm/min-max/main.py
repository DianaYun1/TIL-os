import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    mx = 1
    mn = 10**7
    for num in lst:
        if num > mx:
            mx = num
        if num < mn:
            mn = num

    ans = mx - mn
    print(f'#{tc} {ans}')