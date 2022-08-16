import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = input()
    m = input()
    ans = 0

    for j in range(len(n)):
        for i in range(len(m) - len(n)+1):
            if n[j] == m[i]:
                if n == m[i:i+len(n)]:
                    ans = 1
                    break

    print(f'#{tc} {ans}')