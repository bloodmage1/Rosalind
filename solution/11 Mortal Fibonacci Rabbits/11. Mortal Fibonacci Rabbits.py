import os
os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_fibd.txt") as f:
    a= f.readline()
    n, k = a.split()


n = int(n)
k = int(k)
# n=6
# k= 3
fib = [1] * 100



for i in range(2,n):
    fib[i] = fib[i-1] + fib[i-2]
    if i >= k:
        fib[i] -= fib[i-k-1]
        # print(fib[i-k-1])

print(fib[n-1])