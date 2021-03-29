from sys import stdin
r,c =map(int,input().split())
a=[]
for i in range(r):
    s = [int(x) for x in stdin.readline().split()]
    a.append(s)

b=[]
for i in range(r):
    for j in range(c):
        a[i][j]=str(a[i][j])
        if i == 0:
            b.append(len(a[i][j]))
        else:
            if len(a[i][j]) > b[j]:
                b[j] = len(a[i][j])
for i in range(r):
    for j in range(c):
        tmp = b[j]
        kc = len(a[i][j])
        print(a[i][j].rjust(tmp," "),end=" ")
    print()
