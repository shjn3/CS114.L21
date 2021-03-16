n, m = map(int,input().split())
r, c = map(int,input().split())

if (r*c != n*m):
    for i in range(n):
       q = input()
       print(q)
else:
    a=[]
    for i in range(n):
        q = input()
        a =a+ q.split()
        while len(a)>=c:
            tmp =' '.join(a[:c])
            print(tmp)
            a = a[c:]
