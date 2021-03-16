n = int(input())
k = int(input())
p = int(input())
q = int(input())

alice = p*2
if q == 1:
    alice = alice-1

if k == n:
    print(-1)
elif 2*k<=n:
    if alice - k > 0:
        bob = alice - k
        if bob % 2 == 0:
            print(bob//2,' ',2)
        else:
            print((bob+1)//2,' ',1)
    else:
        bob=alice+k
        if bob % 2 == 0:
            print(bob//2,' ',2)
        else:
            print((bob+1)//2,' ',1)
else:
    if alice - k > 0:
        bob = alice - k
        if bob % 2 == 0:
            print(bob//2,' ',2)
        else:
            print((bob+1)//2,' ',1)
    elif alice + k <=n:
        bob=alice+k
        if bob % 2 == 0:
            print(bob//2,' ',2)
        else:
            print((bob+1)//2,' ',1)
    else:
        print(-1)
