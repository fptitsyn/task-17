f = open("17-341.txt")
a = [int(i) for i in f]

k = 0
kmax = 0

m = sum(a) / len(a)

for i in range(1, len(a)-2):
    if ((a[i] * a[i+1]) > (a[i-1] * a[i+2])):
        kmax = max(kmax, a[i] + a[i+1])
        if (a[i] > m or a[i+1] > m):
            k += 1
        
print(kmax, k)
