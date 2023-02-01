import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    _ = [int(input()) for _ in range(p)]
    bus_stop = [0]*p

    for a, b in arr:
        for i in range(a-1, b):
            bus_stop[i] += 1

    print(f'#{tc}', *bus_stop)