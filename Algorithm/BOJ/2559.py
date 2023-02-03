n, k = map(int, input().split())
lst = list(map(int, input().split()))

s = sum(lst[:k])
ans = s
for i in range(0, n-k):
    s = s - lst[i] + lst[i+k]
    ans = max(s, ans)

print(ans)