import os

import sys


os.chdir(r"C:\Users\user\Desktop")

sys.stdout = open("output.txt", "w")


with open("rosalind_seto.txt") as f:
    ros= f.read().strip().split("\n")

n = int(ros[0])

del ros[0]

a,b   = "t".join(map(str, ros)).split("t")

a = a.replace("{","")
a = a.replace("}","")

split_a = a.split(",")

a = []
for i in split_a:
    a.append(int(i))

a = set(a)

b = b.replace("{","")
b = b.replace("}","")

split_b = b.split(",")
b = []
for i in split_b:
    b.append(int(i))

b = set(b)

print(a|b)

print(a&b)

print(a-b)

print(b-a)

u = {i for i in range(1,n+1)}

print(u-a)

print(u-b)

sys.stdout.close()