f = float(input())
c = (f-32)/1.8
k =c + 273.15
if  c == round(c):
    c= round(c)
    k = round(k,2)
else:
    k= round(k,3)
    if c>2 and c<55:
      c = round(c,5)
    elif c> 55 and c <90:
      c = round(c,4)
    else:
        c = round(c,3)

print(c,' ',k)
