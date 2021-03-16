import math
a = float(input())
b = float(input())
c = float(input())
if a+b <= c or a+c <= b or b+c <= a:
    print('Khong phai tam giac')
else:
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if s == round(s):
        s = round(s)
    else:
        s = round(s,2)
    if a==b and b==c:
        print('Tam giac deu, dien tich =',s)
    elif a==b or a==c or b==c:
        print('Tam giac can, dien tich = ',s)
    elif a*a == (b*b +c*c) or b*b == (a*a +c*c) or c*c == (a*a + b*b):
        print('Tam giac vuong, dien tich = ',s)
    else:
        print('Tam giac thuong, dien tich = ',s)
