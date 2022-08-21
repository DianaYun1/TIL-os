import sys
sys.stdin = open("s_input.txt", "r")

# def b_sort(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#     return arr[len(arr)-1]

T = 10
for ts in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    # sol-1
    # for i in range(2, n-2):
    #     arr = [lst[i+1], lst[i+2], lst[i-1], lst[i-2]]
    #     if lst[i] > b_sort(arr):
    #     # if lst[i] > lst[i+1] and lst[i] > lst[i+2] and lst[i] > lst[i-1] and lst[i] > lst[i-2]:
    #         ans += lst[i] - b_sort(arr)

    # sol-2
    k = 2
    for i in range(k, n-k):
        # mx = max(lst[i-k:i] + lst[i+1:i+k+1]
        mx = lst[i-k]
        for j in range(i-k+1, i+k+1):
            if i != j and mx < lst[j]:
                mx = lst[j]
        if lst[i] > mx:
            ans += lst[i] - mx

    print(f'#{ts} {ans}')


