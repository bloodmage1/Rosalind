import os
import sys

os.chdir(r"C:\Users\user\Desktop")

# sys.stdout= open("output.txt","w")
with open("rosalind_long.txt") as f:
    ros = f.read()

dic = {}
for line in ros.split("\n"):
    if line.startswith(">"):
        a = line
        b = ""
    else:
        b += line
    
    dic[a] = b

ros = []
dict = sorted(dic.items())

for k,v in dict:
    ros.append(v)

# ros1 = ["ATTAGACCTG", "CCTGCCGGAA"]

# print(max("ATTAGACCTG", "CCTGCCGGAA"))
# print(min("ATTAGACCTG", "CCTGCCGGAA"))

# def check(seq1, seq2):
#     m = len(seq1)
#     t = len(seq2)
#     for j in range(t):
#         if seq1[j:j+t-(j-m+t)] == seq2[i][0:t-(j-m+t)]:
#             seq1 += seq2[i][t-(j-m+t):t]
#     return seq1

####################################################

answers = []
main = ros[0]
for i in range(1,len(ros)):
    m = len(main)
    t = len(ros[i])

    if ros[i] in main:
        continue
    else:
        for j in range(t):
            if main[j:j+t-(j-m+t)] == ros[i][0:t-(j-m+t)]:
                main += ros[i][t-(j-m+t):t]
                break
        main += ros[i]

print(main)

######################################################################
# def weld_seq(seq1, seq2):
#     for weld_len in reversed(range(min(len(seq1), len(seq2)))):
#         if seq1[-weld_len:] == seq2[0: weld_len]:
#             return seq1 + seq2[weld_len:]
#     return seq1 + seq2

# while len(ros) > 1:
#     weld_result = []
#     for seq1 in ros:
#         for seq2 in ros:
#             if seq1 == seq2:
#                 continue
#             welded_seq = weld_seq(seq1, seq2)
#             score = abs(len(seq1) + len(seq2) - len(welded_seq))
#             weld_result.append([seq1, seq2, welded_seq, score])
#     max_weld = max(weld_result, key = lambda x: x[3])
#     ros.remove(max_weld[0])
#     ros.remove(max_weld[1])
#     ros.append(max_weld[2])
# print(ros[0])

#####################################################################
# answer = ros[0]
    
# for k in ros:
#     main = max(answer, k)
#     temp = min(answer, k)
#     m = len(main)
#     t = len(temp)

#     for j in range(t):
#         if temp in main:
#             break
#         if j <= m-t :
#             if main[j:j+t] == temp[0:t]:
#                 break
#         else:
#             if main[j:j+t-(j-m+t)] == temp[0:t-(j-m+t)]:
#                 answer += temp[t-(j-m+t):t]
#             else:

# print(answer)



# for i in range(len(ros)):
#     m = len(main)
#     t = len(ros[i])
#     if ros[i] in 

