from sys import stdin

n=[]
while True:
    a = [int(x) for x in stdin.readline().split()]
    lenth = len(a)
    if lenth == 2:
        if a[1] < 1000:
            if a[0] == 0:
                n.insert(0,a[1])
            elif a[0] == 1:
                n.append(a[1])
            elif a[0] == 3:
                if a[1] in n:
                   n.remove(a[1])
            elif a[0] == 4:
                while a[1] in n:
                    n.remove(a[1])
    elif lenth == 3:
        if a[1] in n:
            n.insert(n.index(a[1])+1,a[2])
        else:
            n.insert(0,a[2])
    else:
        if a[0] == 5 and len(n)!=0:
            n.pop(0)
        elif a[0] == 6:
            break
s=' '.join(map(str,n))
print(s)
