q = int(input())
for i in range(0,q):
    n = int(input())
    tmp = input()
    x=tmp.split()
    sum = 0
    for i in range(0,n):
        sum = sum+ int(x[i])
    if sum % n == 0:
        print(sum//n)
    else:
        while sum % n !=0:
            sum = sum+1
        print(sum // n)
