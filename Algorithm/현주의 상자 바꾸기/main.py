import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n, q = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(q)]
    box = [0]*n
    k = 1

    for l, r in arr:
        for i in range(l-1, r):
            box[i] = k
        k += 1

    print(f'#{tc}', *box)