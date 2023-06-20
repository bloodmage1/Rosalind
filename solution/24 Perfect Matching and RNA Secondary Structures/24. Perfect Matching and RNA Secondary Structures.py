import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_pmch.txt") as f:
    a = f.read().strip().split("\n")

ros = a[1] + a[2]

def fac(n):
    if n == 1:
        return 1

    return n * fac(n-1)

print(fac(ros.count("A"))*fac(ros.count("G")))