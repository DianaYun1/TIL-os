import sys
sys.stdin = open("s_input.txt", "r")

tbl = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dct = {tbl[n]: n for n in range(10)}

# T = 10
T = int(input())
for test_case in range(1, T + 1):
    _, N = input().split()
    lst = list(map(str, input().split()))
    # lst = list(input().split())

    # [1] 받은 숫자 자리를 누적
    cnts = [0] * 10
    for st in lst:
        cnts[dct[st]] += 1

    # [2] sols 결과에 개수만큼 str 붙이기
    sols = []
    for i in range(10):
        sols.append((tbl[i] + " ") * cnts[i])

    print(f'#{test_case}')
    print(*sols)