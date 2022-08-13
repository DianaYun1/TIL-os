import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for _ in range(t):
    tc, n = input().split()
    n = int(n)
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = [0]*len(nums)
    lst = list(input().split())
    ans = []

    for l_num in lst:
        for i in range(len(nums)):
            if l_num == nums[i]:
                cnt[i] += 1
    for i in range(len(nums)):
        ans += [nums[i]]*cnt[i]

    print(f'{tc}\n', *ans)