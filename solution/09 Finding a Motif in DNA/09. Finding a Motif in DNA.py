import os 

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_subs.txt") as f:
    sample = f.readlines()
    a= sample[0].strip()
    b= sample[1].strip()

for i in range(0, len(a)):
    if a[i:i+len(b)] == b:
        print(i+1, end =" ")
