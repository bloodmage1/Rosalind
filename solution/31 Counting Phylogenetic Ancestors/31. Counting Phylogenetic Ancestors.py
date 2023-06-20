import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_inod.txt") as f:
    a = f.read().strip()
    
print(int(a) -2)