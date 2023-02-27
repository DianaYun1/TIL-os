c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
else:
    # 6+5=11*2=22 4+3=7*2=14 2+1=3*2=6
    n = (r+1)//2
    s = 0
    for i in range(n):
        s += (c+r-2-i*4)*2
        if s >= k:
            d = i+1

        else:
            continue

