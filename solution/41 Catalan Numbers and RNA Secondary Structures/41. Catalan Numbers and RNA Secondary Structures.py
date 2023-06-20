# import os

# os.chdir(r"C:\Users\user\Desktop")

# with open("rosalind_cat.txt") as f:
#     a =f.read().strip()

# for line in a.split("\n"):
#     if line.startswith(">"):
#         a = line
#         b = ""
#     else:
#         b += line

# 이해 불가능..

b= "CGGCUGCUACGCGUAAGCCGGCUGCUACGCGUAAGC"

b = """AACUCAUGAAUAUGAGCUACGUAUUUGUUUAUAACAUGCUAGGUACCGGCCGUCCGCGGA
UAUAGAUGCCCAUCGUGCAGUUAAGCACCGCGCGCGUAUGGCCAGCGCGGAUCCGGGUCG
ACCAGCGGAUCCGCUUCGAGGCGCAACAUAUGGCCGGCUAUUUUAACCUUGCCACUAGUG
GCCCGGGUAGCCAUCGACGAGAUAUGCCUAUACGAUAUGCAAUUGUAUAGAUCCCUCGAC
GGGGAUGCGCCGCGCGCCUAGUUUUAAAAACAAUAGCUUGGCUAUCGAUCUGCAAU""".replace("\n","")

# b = "UAGCGUGAUCAC"

# print(b.count("AU"), b.count("CG"),b.count("GC"),b.count("UA"))

# def fac(n):
#     answer =1 
#     for i in range(1, n+1):
#         answer *= i
    
#     return answer

# def cat(n):
#     return fac(n*2) // (fac(n+1)*fac(n))

cnt_cg = 0
cnt_au = 0
p = 0
q =0
answer = 0

def cat_(s):
    table = {'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1, '':1}
    if s not in table:
        p = 0
        for i in range(1, len(s), 2):
            if (s[0]+s[i]) in ['AU', 'UA', 'GC', 'CG']:
                print(1)
                p += cat_(s[1:i]) * cat_(s[i+1:])            #the Catalan recursive form
        table[s] =  p % 1000000       
    return table[s]

print(cat_(b))


# while True: 
#     try:
#         p = b.index("C", q, len(b))
#         q=  b.index("G", p, len(b))
#         if b.count("A",p,q) == 0 or b.count("U",p,q) == 0:
#             answer += 1
#             cnt_cg += 1

#     except ValueError:
#         break
# p = 0
# q = 0

# while True: 
#     try:
#         p = b.index("A", q, len(b))
#         q=  b.index("U", p, len(b))
#         cnt_au += 1

#     except ValueError:
#         break
# print(cnt_cg)
# print(cnt_au)
# print(cat(6), cat(7), cat(8), cat(9), cat(10), cat(11), cat(12))


# print((cat(cnt_cg)*cat(b.count("C")-cnt_cg)*cat(cnt_au)*cat(b.count("A")-cnt_au))/736)
# print((cat(3)*cat(3)*cat(6)*cat(6))%1000000)
# print((fac(8)*fac(4)*fac(3)*fac(3))%1000000)

# print(((cat(cnt_cg))*(cat(cnt_au))))

# print((cat(cnt_cg-1))*(cat(cnt_au-1)))
# print((cat(cnt_cg)*cat(1-cnt_au) - cat(1-cnt_cg)*cat(cnt_au))%1000000)
# print((cat(cnt_cg)-cat(1-cnt_cg)))

# n1 = b.count("A")
# n2 = b.count("C")

# print((fac(2*n1) / (fac(n1)*fac(n1+1))*(fac(2*n2) / (fac(n2)*fac(n2+1))))%1000000)



# b = """AGGUACGCGUCGCCGGUAACAUGCCUCGAUCAUAUUAAUGUUUUAAUAAAUGCAAUACGC
# CGGUAUUACCGACGUAUCGGAGCAUUAUAUCGAAUAGCUUAAGGCGCGCCUUGUACGCUA
# GAUUAGCAUGCAUGCGUACGAUAUCGCCUAUAUCUUAAAUUCGAUAGAUUAGUAUGGCGC
# CAUAUAAUAUAUAUCACGUAUAUAGUUGCGCAUAUCGAUUAAAGUACCUCAUAUGCGUUA
# CGCGACAUCAUGUGUCGCGAUAAUCAGACGUCGA""".replace("\n","")

# print(b.count("A"),b.count("C"),b.count("G"),b.count("U"))

# def solve(rna):
#     """
#     An input RNA consisting of {A, U, C, G}
#     The number of non-overlapping perfect 
#     matchings.
#     """
#     return helper(rna, 0, len(rna) - 1, {})


# def helper(rna, lo, hi, dp):
    
#     mapping = {
#     "A" : "U",
#     "U" : "A",
#     "G" : "C",
#     "C" : "G"
#     }
#     characters = hi - lo + 1
    
#     # if there are an odd number of nucleotides, 
#     # this is an invalid matching.
#     if characters % 2 == 1:
#         return 0

#     # handles tricky edge cases.
#     if lo >= hi or lo >= len(rna) or hi < 0:
#         return 1

#     # return answer if it is memoized.    
#     if (lo, hi) in dp:
#         return dp[(lo, hi)]
#     else:
#         curr = rna[lo]
#         target = mapping[curr]
#         acc = 0
#         for i in xrange(lo + 1, hi + 1, 2):
#             if rna[i] == target:
#                 left = helper(rna, lo + 1, i - 1, dp)
#                 right = helper(rna, i + 1, hi, dp)
#                 acc += (left * right) % 1000000
#         dp[(lo, hi)] = acc
#         return acc


# rna = "CAUAUG"

# print solve(rna.strip()) % 1000000