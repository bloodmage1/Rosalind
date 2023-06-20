import os
import sys

os.chdir(r"C:\Users\user\Desktop")

lis = []

with open("rosalind_lexv.txt") as f:
    a =  f.read().strip("\n").split("\n")

dna, n = a[0].split(), int(a[1])

# sys.stdout = open("output.txt", "w")

# from itertools import product

# for i in range(1,n+1):
#     for j in ((product(dna, repeat = i))):
#         for k in j:
#             print(k, end = " ")
#         print()

# sys.stdout.close()

def repi(n, word=""):
    print(word)
    if n == 0:
        return
    for c in dna:
        repi(n-1, word+c)

repi(n)







