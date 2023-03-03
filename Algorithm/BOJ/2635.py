n = int(input())
ans = 0
ans_lst = []

def comp(a, b):
    lst = [a, b]
    while a-b >= 0:
        lst.append(a-b)
        a, b = b, a-b
    return len(lst), lst


for i in range(1, n+1):
    cnt, n_lst = comp(n, i)
    if ans != max(ans, cnt):
        ans = cnt
        ans_lst = n_lst

print(ans)
print(*ans_lst)