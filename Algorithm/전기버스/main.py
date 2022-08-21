import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    charge = [0]*(n+1)
    for i in lst:
        charge[i] = 1

    cnt = 0
    start = k
    while start <= n-k:
        # if 1 == charge[start+1]:
        #     cnt += 1
        #     start = start + 1
        #     # continue
        if 1 in charge[start-k+1:start+1]:
            for i in range(start, start-k):
                if charge[i] == 1:
                    start = i
                    cnt += 1
                    break
                break
            continue

        else:   # 1 not in charge[start-k:start+1]
            cnt = 0
            break

    print(f'#{tc} {cnt}')

'''
T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
 
    lst.append(N)
    start = prev = ans = 0
    for nxt in lst:
        if nxt-prev > K:
            ans = 0
            break
        if nxt-start > K:
            start = prev
            ans += 1
        prev = nxt
    # while
    # i = ans = start = last = 0
    # while i<M+1:
    #     if lst[i]-start <= K: # start ~ 현재위치 이동가능
    #         last = lst[i]
    #         i += 1
    #     else:
    #         if lst[i]-last > K: # 불가능한경우 0출력
    #             ans = 0
    #             break
    #         else:
    #             start = last
    #             ans += 1
    print(f'#{test_case} {ans}')
'''