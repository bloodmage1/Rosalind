ros = "TCAATGCATGCGGGTCTATATGCAT"

import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_revp.txt") as f:
    ros = f.read().strip()

ros1 = ros.split("\n")[1:]

ros = ""

for i in ros1:
    ros += i

def trans(a):
    a_reverse = a[::-1]

    a_reverse1 = a_reverse.replace("A","t")
    a_reverse2 = a_reverse1.replace("C","g")
    a_reverse3 = a_reverse2.replace("G","c")
    a_reverse4 = a_reverse3.replace("T","a")

    a = a_reverse4.upper()
    return a

for i in range(len(ros)):
    for j in range(2,7):
        if ros[i:i+j] == trans(ros[i+j:i+j+j]):
            index = i+1
            leng = j*2
        
        else:
            continue
        print(index, leng)