n, m, a = map(int,input().split())

hang = 0
cot  = 0
if m % a == 0:
    hang = m//a
else:
    hang = m//a + 1
if n % a == 0:
    cot = n//a
else:
    cot = n//a + 1

print(hang*cot)
