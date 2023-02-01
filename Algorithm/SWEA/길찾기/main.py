import sys
sys.stdin = open("s_input.txt", "r")

def dfs(s):
    visited[s] = 1
    stk = []

    while True:
        for visit in arr[s]:
            if not visited[visit]:
                stk.append(s)
                visited[visit] = 1
                s = visit
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break

t = 10
for tc in range(1, t + 1):
    _, n = map(int, input().split())
    st = list(map(int, input().split()))
    arr = [[] * 2 for _ in range(100)]
    s, e = 0, 99

    for i in range(0, len(st), 2):
        arr[st[i]].append(st[i+1])

    visited = [0]*100
    dfs(s)

    print(f'#{tc} {visited[e]}')