import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_mmch.txt") as f:
    a =f.read().strip()

for line in a.split("\n"):
    if line.startswith(">"):
        a = line
        b = ""
    else:
        b += line

    ros = b


def fac(n, k):
    answer = 1
    if n> k:
        for i in range(n-k+1, n+1):
            answer *= i        
    else:
        for i in range(k-n+1, k+1):
            answer *= i
    return answer

print(fac(ros.count("A"), ros.count("U"))*fac(ros.count("G"), ros.count("C")))


