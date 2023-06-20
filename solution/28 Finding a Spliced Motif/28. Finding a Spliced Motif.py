import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_sseq.txt") as f:
    a = f.read()

dic = {}

for line in a.split("\n"):
    if line.startswith(">"):
        a = line
        b = ""

    else:
        b += line
    dic[a] = b

ros = []

for k,v in dic.items():
    ros.append(v)

a = ros[0]
b = ros[1]

p = 0
for i in b:

    print(a.index(i, p, len(a))+1)
    p = a.index(i, p, len(a))+2 


