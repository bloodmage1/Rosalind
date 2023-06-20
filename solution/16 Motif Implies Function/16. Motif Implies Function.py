from re import finditer
from sys import argv
from urllib.request import urlopen

uniprot = "http://www.uniprot.org/uniprot/%s.fasta"

# for i in open(argv[1:]):
#     print(i)
# print(argv[1])

args = argv
for i in args:
    print(i)

