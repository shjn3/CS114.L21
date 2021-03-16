psi = float(input())
if psi > 0:
    kq = psi * (0.453592/(2.54*2.54))
    if psi < 10:
        print(round(kq,5))
    elif psi>=10 and psi <1000:
       print(round(kq,4))
    elif psi >=1000 and psi <12000:
        print(round(kq,3))
    else:
        print(round(kq,2))
