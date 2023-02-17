n = int(input())
stu = []
lst = list(map(int, input().split()))

for i in range(n):
    stu.insert(i-lst[i], i+1)

print(*stu)