import sys
sys.stdin = open("s_input.txt", "r")


def dfs(arr, s, g, visited, need_visited):
    visited[s] = 1
    if g in arr[s]:
        return 1
    else:
        for i in arr[s]:
            need_visited.append(i)
        while need_visited:
            i = need_visited.pop()
            if visited[i] == 0:
                return dfs(arr, i, g, visited, need_visited)
    return 0


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())

    visited = [0]*(v+1)
    need_visited = [0]*(v+1)
    ans = dfs(graph, s, g, visited, need_visited)

    print(f'#{tc} {ans}')