import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    str1 = list(set(input()))
    str2 = input()
    cnt = [0]*len(str1)
    mx = 0

    for i in range(len(str1)):
        for m in str2:
            if str1[i] == m:
                cnt[i] += 1
                if mx < cnt[i]:
                    mx = cnt[i]

    print(f'#{tc} {mx}')