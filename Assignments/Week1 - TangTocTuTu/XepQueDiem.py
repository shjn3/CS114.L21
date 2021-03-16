q = int(input())
for i in range(0,q):
    n = int(input())
    tong = 0
    if n % 2 != 0:
        n = n +1
        tong = tong +1
    k = 0
    while k < 100:
        c = (n + k)//2
        b = (c + 1)//2
        a = c - b
        if a + b + c == n+k and a != 0:
            print(tong)
            break
        k = k+2
        tong = tong + 2
