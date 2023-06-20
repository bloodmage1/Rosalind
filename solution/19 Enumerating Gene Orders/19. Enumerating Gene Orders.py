import os 

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_perm.txt") as f:
    n = int(f.read().strip())

from itertools import permutations

numbers = [i+1 for i in range(n)]

def per(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer
print(per(n))

for i in permutations(numbers):
    for j in i:
        print(j, end = " ")
    print()