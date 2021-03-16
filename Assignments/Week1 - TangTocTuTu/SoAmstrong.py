n = int(input())
if n >=0:
    i = 1
    while n // 10**i > 0:
        i=i+1
    tmp = n
    sum = 0
    while tmp > 0:
        last = tmp % 10
        sum = sum + last**i
        tmp = tmp // 10
    if sum == n:
        print('True')
    else:
        print('False')
