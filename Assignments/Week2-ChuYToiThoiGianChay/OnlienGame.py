n=set()
while True:
    q = list(map(int,input().split()))
    if q[0]== 0:
        break
    elif q[0] == 1:
        if (q[1] not in n):
            n.add(q[1])
    else:
        if (q[1] in n):
            print(1)
        else:
            print(0)
