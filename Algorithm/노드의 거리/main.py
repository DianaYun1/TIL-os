import sys
sys.stdin = open("s_input.txt", "r")


def bfs(S):
    visited[S] = 1
    q = []
    q.append((S, 0))
    while q:
        c, ans = q.pop(0)
        if c == E:
            return ans
        for n in arr[c]:
            if not visited[n]:
                q.append((n, ans+1))
                visited[n] = 1
    return 0

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    arr = [[]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, g = map(int, input().split())
        arr[s].append(g)
        arr[g].append(s)
    S, E = map(int, input().split())

    visited = [0]*(V+1)
    ans = bfs(S)

    print(f'#{tc} {ans}')