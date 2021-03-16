def uocsochung(a,b):
    if a<b:
        c = a
        a = b
        b = c
    kq = 0
    while b != 0:
        kq = a - b
        a = b
        b = kq
        if a < b:
            c = a
            a = b
            b = c
    return a

n = int(input())
for x in range(0,n):
    a, b = map(int,input().split())
    if a % b == 0:
         print(a//b)
    else:
        uoc = uocsochung(a,b)
        print(a//uoc,' ',b//uoc)
