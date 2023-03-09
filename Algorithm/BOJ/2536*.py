import collections
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())

bus = [0] * (k+1)
adj = [[] for _ in range(k+1)]

for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    bus[b] = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

sx, sy, dx, dy = map(int, input().split())

check = [False] * (k+1)  # 더 큰 버스에 포함되는지 확인
for i in range(1, k+1):
    tmp = False
    x1, y1, x2, y2 = bus[i]
    for j in range(1, k+1):
        if i == j:
            continue
        x3, y3, x4, y4 = bus[j]
        # 수직버스
        if x1 == x2 == x3 == x4:
            if y3 <= y1 <= y2 <= y4:
                tmp = True
        # 수평버스
        if y1 == y2 == y3 == y4:
            if x3 <= x1 <= x2 <= x4:
                tmp = True

    check[i] = tmp

for i in range(1, k+1):
    # 이미 포함되는 버스면 continue
    if check[i]:
        continue
    x1, y1, x2, y2 = bus[i]
    for j in range(1, k+1):
        # 이미 포함되는 버스면 continue
        if check[j]:
            continue
        if i == j:
            continue
        x3, y3, x4, y4 = bus[j]
        # 한 점에서 만나는 경우 (방향이 서로 다른 경우)
        if (x1 <= x3 <= x2 and y3 <= y1 <= y4) or (x3 <= x1 <= x4 and y1 <= y3 <= y2):
            adj[i].append(j)
            adj[j].append(i)
        # 한 점 혹은 겹치는 경우 (수평 방향)
        if y1 == y2 == y3 == y4:
            if not(x1 > x4 or x2 < x3):
                adj[i].append(j)
                adj[j].append(i)
        # 한 점 혹은 겹치는 경우 (수직 방향)
        if x1 == x2 == x3 == x4:
            if not(y1 > y4 or y2 < y3):
                adj[i].append(j)
                adj[j].append(i)

start = []
end = []
for i in range(1, k+1):
    if check[i]:
        continue
    x1, y1, x2, y2 = bus[i]
    if x1 <= sx <= x2 and y1 <= sy <= y2:
        start.append(i)
    if x1 <= dx <= x2 and y1 <= dy <= y2:
        end.append(i)

q = collections.deque()
visit = [-1] * (k+1)
for i in start:
    q.append(i)
    visit[i] = 0
while q:
    now = q.popleft()
    for nxt in adj[now]:
        if visit[nxt] == -1:
            visit[nxt] = visit[now] + 1
            q.append(nxt)

ans = k
for i in end:
    ans = min(ans, visit[i])
print(ans+1)