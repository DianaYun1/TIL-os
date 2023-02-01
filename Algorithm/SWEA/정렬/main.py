import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    # selection sort
    for i in range(n-1):
        # i ~ 끝까지 가장 작은 값의 index
        i_min = i
        for j in range(i+1, n):
            if lst[i_min] > lst[j]:
                i_min = j
        # i <-> i_min 자리의 값 교환
        lst[i], lst[i_min] = lst[i_min], lst[i]

    print(f'#{tc}', *lst)