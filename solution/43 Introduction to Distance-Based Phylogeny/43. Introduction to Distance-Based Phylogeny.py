import os
import sys

os.chdir(r"C:\Users\user\Desktop")

# sys.stdout= open("output.txt","w")
with open("rosalind_pdst.txt") as f:
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

answers = []
for i in lis:
    leng = len(i)
    answer = []
    for j in lis:
        wrong = 0
        for k in range(leng):
            if i[k] != j[k]:
                wrong += 1
        answer.append(round(wrong/leng, 3))

    answers.append(answer)

for i in range(len(answers)):
    for j in range(len(answers[i])):
        print(answers[i][j], end = " ")
    print()



            
