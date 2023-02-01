lst = []
for _ in range(9):
    lst.append(int(input()))
    
lst.sort()
n = sum(lst) - 100

for i in range(9):
    if n-lst[i] in lst:
        if lst[i] != n-lst[i] :
            lst.remove(n-lst[i])
            lst.remove(lst[i])      # 같은 값이 있어도 리스트 젤 앞에부터 순차로 지워짐
            break
        elif lst[i] == n-lst[i] and lst.count(lst[i]) >= 2:
            del lst[i+1]    # lst.remove(lst[i]) 2번해도 됨
            del lst[i]
            break
    
for h in lst:
    print(h)