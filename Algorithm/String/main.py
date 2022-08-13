import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

for t in range(10):
    T = int(input())
    target = input()
    st = input()
    m, n = len(target), len(st)

    i = j = 0
    while j < m and i < n:
        if st[i] != target[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m:
        ans = i - m
    else:
        ans = -1

    print(f'#{T} {ans}')