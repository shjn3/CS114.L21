def soganx(a,x,k):
    vt = 0
    e=[]
    lenth = len(a)
    tmp = abs(x-a[0])
    for i in range(1,lenth):
        if tmp > abs(x-a[i]):
            tmp = abs(x-a[i])
            vt = i
    e.append(a[vt])
    low = 1
    high = 1
    for i in range(1,k):
        if (vt-low) >=0 and (vt + high) <=lenth-1:
            tmp1 = abs(x-a[vt-low])
            tmp2 = abs(x-a[vt+high])
            if tmp1 > tmp2:
                e.append(a[vt+high])
                high = high + 1
            elif tmp1 <=tmp2:
                e.append(a[vt-low])
                low = low + 1
        elif vt-low < 0:
            e.append(a[vt+high])
            high = high + 1
        elif vt+high >len(a)-1:
            e.append(a[vt-low])
            low = low +1
    return e
        
        
n = int(input())
q = input()
tmp = q.split()
if n == len(tmp):
    a = []
    for i in range(0,len(tmp)):
        a.append(int(tmp[i]))
    k, x = map(int,input().split())
    b = []
    b = soganx(a,x,k)
    b.sort()
    s = ' '.join(map(str,b))
    print(s)
