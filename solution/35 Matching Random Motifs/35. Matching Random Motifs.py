import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_rstr.txt") as f:
    n, prob, seq = f.read().split()

n= int(n)
prob = float(prob)

dic = {}

dic["A"] = (1-prob)/2
dic["C"] = prob/2
dic["G"] = prob/2
dic["T"] = (1-prob)/2

answer = 1

for i in seq:
    answer *= dic[i]

print(round(1- (1-answer)**(n-len(seq)+1), 3))
