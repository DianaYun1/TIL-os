import sys
sys.stdin = open("s_input.txt", "r")


# [1] stack 사용
def dfs(s):
    stk = []
    visited[s] = 1

    while True:
        for e in graph[s]:
            if not visited[e]:
                stk.append(s)       # 되돌아올 위치 백업
                visited[e] = 1      # 방문 기록
                s = e
                break
        else:
            if stk:     # stk에 남아있으면 꺼내기
                s = stk.pop()
            else:       # 없으면 끝
                break


# [2] recursive
def dfs_recur(s):
    # 기준에서 연결된 방문안한 노드 찾으면 방문
    for e in graph[s]:
        if not visited[e]:
            visited[e]=1
            dfs_recur(e)


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    s, g = map(int, input().split())

    visited = [0]*(v+1)
    dfs(s)

    print(f'#{tc} {visited[g]}')