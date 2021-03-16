a = input()
b = input()
c = len(a)
if c == len(b):
    for i in range(0,c):
        if a[i] != b[c-i-1]:
            print("NO")
            break
        if i == c-1:
            print("YES")
else:
    print("NO")
