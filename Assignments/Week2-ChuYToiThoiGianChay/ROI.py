h,w = map(int,input().split())
a = []
b = []
for _ in range(h):
    a.append(list(map(int,input().split())))
    b.append([0]*w)
top,left,bottom,right = map(int,input().split())

for i in range(top,bottom+1):
    for j in range(left,right+1):
        b[i][j] = a[i][j]

for i in b:
    s =' '.join(map(str,i))
    print(s)
