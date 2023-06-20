import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_sset.txt") as f:
    a = f.read().strip()

print((2**int(a))%1000000)