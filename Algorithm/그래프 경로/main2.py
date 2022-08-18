import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())

    stk = []
    visit = [0] * (v+1)
    stk.append(s)
    while stk:
        node = stk.pop()
        visit[node] = 1
        for i in graph[node]:
            if not visit[i]:
                stk.append(i)
    ans = visit[g]

    print(f'#{tc} {ans}')