def f(n):
    if n <=1: return n
    else: return f(n-1)+f(n-2)
n=int(input())
if n < 1 or n > 30:
    print ('So ',n,' khong nam trong khoang [1,30].')
else:
    print(f(n))
