q=int(input())
for i in range(q):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    lenth = len(a)
    dem =0
    for j in range(lenth):
        if a[j]==k:
            dem = dem +1
    print(dem)
