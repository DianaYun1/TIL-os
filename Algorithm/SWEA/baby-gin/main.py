import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input()))
    cnts = [0] * 12

    ans = 0
    # cnts 배열에 빈도수 표기
    for n in lst:
        cnts[n] += 1

    # tri, run 찾기
    i = 0
    while i < 10:
        if cnts[i] >= 3:
            ans += 1
            cnts[i] -= 3
        elif cnts[i] >= 1 and cnts[i + 1] >= 1 and cnts[i + 2] >= 1:
            ans += 1
            cnts[i] -= 1
            cnts[i + 1] -= 1
            cnts[i + 2] -= 1
        else:
            i += 1
    print(f'#{tc} {ans//2}')