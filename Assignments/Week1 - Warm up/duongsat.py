k, t = map(int, input().split())
if t > 0 and t <=10**9 and k>0 and k <=10**9:
    if t <= k:
        print(t)
    else:
        chieu = t // k
        ga = t % k
        if chieu % 2 == 0:
           print(ga)
        else:
           print(k-ga)
