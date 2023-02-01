for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    rec1 = [[x1, q1], [x1, y2], [p1, y1], [p1, q1]]
    rec2 = [[x2, q2], [x2, y2], [p2, y2], [p2, q2]]
    
    if rec1[0] == rec2[2] or rec1[1] == rec2[3] or rec1[2] == rec2[0] or rec1[3] == rec2[1]:
        print('c')
    elif p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1 :
        print('d')
    elif q1 == y2 or q2 == y1 or p1 == x2 or x1 == p2:
        print('b')
    else:
        print('a')
    
