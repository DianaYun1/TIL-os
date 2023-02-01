import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(1, N+1):
        s = 1
        for j in range(1, i+1):
            print(s, end=' ')
            s = s * (i - j) // j
        print()