import os

os.chdir(r"C:\Users\user\Downloads")

with open("rosalind_revc.txt") as f:
    a = f.readline()

a_reverse = ""

for i in a:
    a_reverse = i + a_reverse

# a_reverse = a[::-1]

a_reverse1 = a_reverse.replace("A","t")
a_reverse2 = a_reverse1.replace("C","g")
a_reverse3 = a_reverse2.replace("G","c")
a_reverse4 = a_reverse3.replace("T","a")

a = a_reverse4.upper()


print(a)


# ########## 2222222222222 ##############

# from Bio.Seq import Seq

# coding_dna = Seq(a)
# print(coding_dna.reverse_complement())

# ########## 3333333333333 ##############

# a_reverse = a.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()[::-1]

# print(a_reverse)


# ########## 44444444444444 ##############

# complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
# result = [] 
# for i in a[::-1].replace("\n",""): 
#     result.append(complement[i])
# print(''.join(result))
