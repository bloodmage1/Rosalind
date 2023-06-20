import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_aspc.txt") as f:
    a, b = f.read().split()
a = int(a)
b = int(b)

def combi(a, b):
    answer =1
    if b== 0:
        return 1
    else:
        for i in range(a-b+1, a+1):
            answer *= i
        for i in range(a-b+1, a+1):
            answer //= a+1-i
    return answer

answer = 0

for i in range(a-b+1):

    answer += combi(a, i)

print(answer%1000000)
