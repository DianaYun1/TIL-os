import sys
sys.stdin = open("s_input.txt", "r")

while True:
    try:
        tc = int(input())
        lst = [list(map(int, input().split())) for _ in range(100)]

        ans = s3 = s4 = 0
        for i in range(100):
            s1 = s2 = 0
            for j in range(100):
                s1 += lst[i][j]
                s2 += lst[j][i]
                if ans < s1:
                    ans = s1
                if ans < s2:
                    ans = s2

            s3 += lst[i][i]
            s4 += lst[i][99-i]
            if ans < s3:
                ans = s3
            if ans < s4:
                ans = s4


        # for j in range(100):
        #     s = 0
        #     for i in range(100):
        #         s += lst[i][j]
        #     if ans < s:
        #         ans = s
        #
        # s = 0
        # for i in range(100):
        #     s += lst[i][i]
        #     if ans < s:
        #         ans = s
        #
        # s = 0
        # for i in range(100):
        #     s += lst[i][99-i]
        #     if ans < s:
        #         ans = s

        print(f'#{tc} {ans}')

    except:
        break