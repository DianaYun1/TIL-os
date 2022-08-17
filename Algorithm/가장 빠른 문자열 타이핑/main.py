import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    a, b = input().split()
    i = cnt = 0
    while i < len(a):
        if a[i:i+len(b)] == b:
            i += len(b)
        else:
            i += 1
        cnt += 1

    print(f'#{tc} {cnt}')