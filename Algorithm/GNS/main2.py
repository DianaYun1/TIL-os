import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for _ in range(t):
    tc, n = input().split()
    lst = list(input().split())
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    ans = []

    for i in range(len(nums)):
        for lst_num in lst:
            if nums[i] == lst_num:
                ans.append(lst_num)

    print(tc)
    print(*ans)
