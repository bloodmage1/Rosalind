import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_cons.txt") as f:
    a = f.read()
dic = {}

for line in a.split("\n"):
    if line.startswith(">"):
        a = line[1:].strip()
        b=""
    else:
        b += line.strip()

    dic[a] = b

answer = {}

top = []
A = ["A:"]
C = ["C:"]
G = ["G:"]
T = ["T:"]

for i in range(len(list(dic.values())[0])):
    count_a =0
    count_c =0
    count_g =0
    count_t =0
    for j in dic.values():
        if j[i] == "A":
            count_a += 1
        if j[i] == "C":
            count_c += 1
        if j[i] == "G":
            count_g += 1
        if j[i] == "T":
            count_t += 1
    if max(count_a, count_c, count_g, count_t) == count_a:
        tp = "A"
    if max(count_a, count_c, count_g, count_t) == count_c:
        tp = "C"
    if max(count_a, count_c, count_g, count_t) == count_g:
        tp = "G"
    if max(count_a, count_c, count_g, count_t) == count_t:
        tp = "T"
    
    top.append(tp)
    A.append(count_a)
    C.append(count_c)
    G.append(count_g)
    T.append(count_t)

for i in top:
    print(i, end ="")
print()
for i in A:
    print(i, end = " ")
print()
for i in C:
    print(i, end = " ")
print()
for i in G:
    print(i, end = " ")
print()
for i in T:
    print(i, end = " ")



