q = int(input())
for i in range(0,q):
  s = input()
  t = input()
  leng=len(s)
  if len(s) != len(t):
      print("NO")
  else:
    for i in range(0,leng):
        if t.find(s[i]) != -1:
            print("YES")
            break
        if i == leng-1:
            print("NO")
