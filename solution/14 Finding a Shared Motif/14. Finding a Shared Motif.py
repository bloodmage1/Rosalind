ros = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

word = []

import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_lcsm.txt") as f:
    ros = f.read()
value = ""
for line in ros.split("\n"):
    if line.startswith(">"):
        word.append(value)
        value = ""
        pass
    else:
        value += line
word.pop(0)

def common_substr(seq_0, word, mid):
    for start in range(len(seq_0) - mid + 1):
        part = seq_0[start:start+mid]

        for seq in word:
            if part not in seq:
                break
        
        else:
            return part
    
    return ""

seq_0 = word.pop(0)

left = 0
right = len(seq_0) + 1

while left +1 < right:
    mid = (left+right) //2
    if common_substr(seq_0, word, mid) != "":
        left = mid
    else:
        right = mid

print(common_substr(seq_0, word, left))








# array = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
# max_word = 0
# index = 0


# for i in range(len(word1)):
#     for j in range(len(word2)):
#         if word1[i] == word2[j]:
#             array[i+1][j+1] = array[i][j] + 1
#         if max_word < array[i+1][j+1]:
#             max_word = array[i+1][j+1]
#             index = i+1
#         print(index)
# print(word1[index-max_word:index])






