
import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_iev.txt") as f:
    a,b,c,d,e,t = f.read().strip().split()


def Expect(a,b,c,d,e,t):
    return (a*2+b*2+c*2+d*1.5+e)
print(Expect(int(a),int(b),int(c),int(d),int(e),int(t)))