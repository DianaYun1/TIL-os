import sys
sys.stdin = open("s_input.txt", "r")

for t in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[-1][i] == 2:
            j = i

    i = 99
    while i > 0:
        if j > 0 and arr[i][j-1] == 1:
            arr[i][j] = 0
            j -= 1
        elif j < 99 and arr[i][j+1] == 1:
            arr[i][j] = 0
            j += 1
        else:
            i -= 1

    print(f'#{T} {j}')

    '''
    N = 100
    # 좌우에 0의 여유공간을 넣어서 입력받는경우, 범위체크 안해도 됨
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(N)]
 
    # 초기값 설정
    i, j = N-1, 0
    # [1] 목적지(출발지) arr[][] == 2
    for tj in range(N+2):
        if arr[i][tj]==2:
            j = tj;
            break
 
    while i>0:
        if arr[i][j-1]==1:    #왼쪽에 이동가능한 길이 있음
            arr[i][j]=0
            j-=1
        elif arr[i][j+1]==1:   # 오른쪽방향 이동가능 체크
            arr[i][j]=0
            j+=1
        else:
            i-=1
 
    print(f'#{test_case} {j-1}')
    '''