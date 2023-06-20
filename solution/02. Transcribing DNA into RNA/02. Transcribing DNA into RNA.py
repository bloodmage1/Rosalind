import os

os.chdir(r"C:\Users\user\Downloads")

with open("rosalind_rna.txt") as f:
    a = f.readline()

print(a.replace("T","U"))
