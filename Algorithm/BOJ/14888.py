import itertools

n = int(input())
# lst = list(map(int, input().split()))
num = list(input().split())
pl, mi, mu, di = map(int, input().split())
sign = []
if pl:
    for i in range(pl):
        sign.append('+')
if mi:
    for i in range(mi):
        sign.append('-')
if mu:
    for i in range(mu):
        sign.append('*')
if di:
    for i in range(di):
        sign.append('//')

signs = list(itertools.permutations(sign))
result = [int(num[0])]*len(signs)


for j in range(len(signs)):
    si = signs[j]
    for i in range(n-1):
        ans = result[j]
        if ans < 0 and si[i] == '//':
            ans = -ans
            ans = str(ans)
            ans += si[i] + num[i+1]
            result[j] = -eval(ans)

        else:
            ans = str(ans)
            ans += si[i] + num[i+1]
            result[j] = eval(ans)

print(max(result))
print(min(result))

