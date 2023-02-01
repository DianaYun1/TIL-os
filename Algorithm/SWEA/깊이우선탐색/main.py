import sys
sys.stdin = open("s_input.txt", "r")

def dfs(v, ans):
    ans.append(v)
    visited[v] = 1
    for w in arr[v]:
        if visited[w] == 0:
            dfs(w, ans)
    return ans

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    n = v+1
    arr = [[] for _ in range(n)]
    ans = []
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    visited = [0]*n
    ans = []
    dfs(1, ans)

    print(f'#{tc}', *ans)