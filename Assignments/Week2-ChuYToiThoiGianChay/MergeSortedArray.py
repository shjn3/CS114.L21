a, b = map(int, input().split())
q = input()
q2 = input()
s = q+' '+q2
tmp = s.split()
lenth = len(tmp)
a=[]
for i in range(0,lenth):
    a.append(int(tmp[i]))
a.sort()
c=[]
for i in range(0,lenth):
    c.append(str(a[i]))
c = ' '.join(c)
print(c)
