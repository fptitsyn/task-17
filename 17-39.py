def f(x , q):
    a = []
    while x > 0:
        a.append(x % q)
        x //= q
    return a[::-1]  # list(reversed(a))


k = 0
kmax = 0

for i in range(3466, 9081+1):
    if (len(f(i, 8)) != len(f(i, 10))) and (i % 7 == 1 or i % 7 == 5):
        k += 1
        kmax = max(kmax, i)
        
print(k, kmax)
