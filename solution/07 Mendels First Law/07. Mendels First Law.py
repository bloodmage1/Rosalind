
import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_iprb.txt") as f:
    a = f.read()
a = a.strip()

q,w,e = a.split()

def cal(q,w,e):
    return 1-((w/(q+w+e))*((w-1)/(q+w+e-1))*(1/4) + (w/(q+w+e))*((e)/(q+w+e-1)) + (e/(q+w+e))*((e-1)/(q+w+e-1)))

print(cal(int(q),int(w),int(e)))
