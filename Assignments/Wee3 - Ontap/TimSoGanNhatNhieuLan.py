import bisect
from sys import stdin
def soganx(a,x,k):
    lenth = len(a)
    if x <a[0]:
        print(a[0],a[k-1])
        return
    elif x> a[-1]:
        print(a[-k],a[-1])
        return
    vt = bisect.bisect_left(a,x,0,len(a))
    left = vt
    right = vt+1
    for i in range(k):
        if left >=0 and right <=lenth-1:
            if x-a[left]<=a[right]-x:
                left -=1
            else:
                right +=1
        elif left < 0:
            left = -1
            right = k
            break
        elif right == lenth:
            left = -k-1
            right = 0
            break
        
    print(a[left+1],a[right-1])
        

n = int(input())
a = list(map(int,stdin.readline().split()))
while True:
    _input= input()
    if _input =="":
        break
    tmp = _input.split()
    k = int(tmp[0])
    x = int(tmp[1])
    soganx(a,x,k)
