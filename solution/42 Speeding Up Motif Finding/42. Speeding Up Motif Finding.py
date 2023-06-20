import os

os.chdir(r"C:\Users\user\Desktop")

import sys

sys.stdout = open("output.txt", "w")

with open("rosalind_kmp.txt") as f:
    a =f.read().strip()

for line in a.split("\n"):
    if line.startswith(">"):
        b = line
        a = ""
    else:
        a += line

answer = [0 for i in range(len(a))]
cnt = 0

for k in range(1, len(a)):
    cnt = 0
    if a[0] == a[k]:
        cnt += 1
        if cnt >= answer[k]:
            answer[k] = cnt
        for j in range(k, len(a)):
            if a[j-k+1] == a[j+1]:
                cnt +=1
                if cnt >= answer[j+1]:
                    answer[j+1] =cnt

            else:
                break
    


for i in answer:
    print(i, end = " ")


sys.stdout.close()