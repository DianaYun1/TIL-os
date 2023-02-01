import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    n = v+1
    graph = [[] for _ in range(n)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*n
    stack = []