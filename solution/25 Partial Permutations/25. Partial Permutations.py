import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_pper_1_dataset.txt") as f:
    n, k = f.read().split()

def perm(n, k):
    answer = 1
    for i in range(n-k+1, n+1):
        answer *= i
    
    return answer

print(perm(int(n), int(k))%1000000)

