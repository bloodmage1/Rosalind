import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_hamm.txt") as f:
    hamm = f.readlines()
    a = hamm[0].strip() 
    b = hamm[1].strip()

count = 0
for i,j in zip(a,b):
    if i != j:
        count += 1

print(count)