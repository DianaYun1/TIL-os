n = int(input())
for i in range(n):
    a = input().split()
    b = input().split()
    a.pop(0)
    b.pop(0)

    if a.count('4') != b.count('4'):
        if a.count('4') > b.count('4'):
            ans = 'A'
        else:
            ans = 'B'
    elif a.count('3') != b.count('3'):
        if a.count('3') > b.count('3'):
            ans = 'A'
        else:
            ans = 'B'
    elif a.count('2') != b.count('2'):
        if a.count('2') > b.count('2'):
            ans = 'A'
        else:
            ans = 'B'
    elif a.count('1') != b.count('1'):
        if a.count('1') > b.count('1'):
            ans = 'A'
        else:
            ans = 'B'
    else:
        ans = 'D'

    print(ans)

