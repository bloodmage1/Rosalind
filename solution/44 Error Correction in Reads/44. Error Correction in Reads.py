import os
import sys

os.chdir(r"C:\Users\user\Desktop")

# sys.stdout= open("output.txt","w")
with open("rosalind_corr.txt") as f:
    ros = f.read()

dic = {}
for line in ros.split("\n"):
    if line.startswith(">"):
        a = line
        b = ""
    else:
        b += line
    
    dic[a] = b

lis = []

for k,v in dic.items():
    lis.append(v)

lis_reverse = []

def trans(a):
    a_reverse = a[::-1]

    a_reverse1 = a_reverse.replace("A","t")
    a_reverse2 = a_reverse1.replace("C","g")
    a_reverse3 = a_reverse2.replace("G","c")
    a_reverse4 = a_reverse3.replace("T","a")

    a = a_reverse4.upper()
    return a

for i in lis:
    lis_reverse.append(trans(i))

leng = len(lis[0])

hamming_1 = []
hamming_2 = []

for i in lis:
    for j in lis:
        wrong = 0
        for k in range(leng):
            if i[k] != j[k]:
                wrong += 1

        if wrong == 1 and (lis.count(i) == 1 or lis.count(j) == 1):
            hamming_1.append([i,j])

    for j in lis_reverse:
        error = 0
        for k in range(leng):
            if i[k] != j[k]:
                error += 1

        if error == 1 and lis.count(i) == 1 and lis_reverse.count(j) >= 1:
            hamming_2.append([i,j])

print(lis)
print(lis_reverse)

hamming_1 = list(set([tuple(set(hamming)) for hamming in hamming_1]))
hamming_2 = list(set([tuple(set(hamming)) for hamming in hamming_2]))

print(hamming_1)
print(hamming_2)

for i in range(len(hamming_1)):
    if hamming_1[i][0] in lis_reverse:
        print(hamming_1[i][1]+"->"+hamming_1[i][0])
    else:
        print(hamming_1[i][0]+"->"+hamming_1[i][1])

for i in range(len(hamming_2)):
    if hamming_2[i][0] in lis_reverse:
        print(hamming_2[i][1]+"->"+hamming_2[i][0])
    else:
        print(hamming_2[i][0]+"->"+hamming_2[i][1])
