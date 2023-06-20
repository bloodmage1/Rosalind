import os
import sys

sys.stdout = open("output.txt", "w")

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_sign.txt") as f:
    n = f.read()
n = int(n)

lis = []

for i in range(-n, n+1):
    lis.append(i)

lis.remove(0)

from itertools import permutations

ros = list(permutations(lis, n))

answer = []

for i in ros:
    count = 0
    for j in range(len(i)):
     
        if i[j]*(-1) in i:
            pass
        else:
            count += 1

    if count == n:
        answer.append(i)

answer = set(answer)

print(len(answer))

for i in answer:
    for j in i:
        print(j, end=" ")
    print()

sys.stdout.close()