import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_tree.txt") as f:
    a = list(f.read().split())

length = int(a[0])


del a[0]

for i in range(len(a)):
    a[i] = int(a[i])

t = []

for i in range(0, len(a),2):
    t.append([a[i], a[i+1]])

print(length - len(t) - 1)

