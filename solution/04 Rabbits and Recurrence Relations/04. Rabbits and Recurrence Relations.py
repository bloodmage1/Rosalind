import os
os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_fib.txt") as f:
    a = f.readline()
    n, k = a.split()
    
print(n,k)
    

fib_array = [1] * 100

for i in range(1,int(n)):
    fib_array[i] = fib_array[i-1] + fib_array[i-2]*int(k)
    
print(fib_array[int(n)-2])
    
  
    
    