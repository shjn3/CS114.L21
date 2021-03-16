from sys import stdin
n = set()
while True:
    q = [int(x) for x in stdin.readline().split()]
    if len(q) == 0:
        continue
    else:
        if q[0] == 0:
           break
        elif q[0] == 1:
           b=q[1]
           n.add(b)
        elif q[0] == 2:
            if q[1] in n:
               print(1)
            else:
               print(0)
        else:
           if q[1] in n and len(q)==2: 
              n.remove(q[1])
