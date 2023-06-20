from bisect import bisect_left
import os
import sys

os.chdir(r"C:\Users\user\Desktop")

sys.stdout= open("output.txt","w")

with open("rosalind_lgis.txt") as f:
    a= f.read().split()
nums = []
for i in a:
    nums.append(int(i))

n = nums[0]
del nums[0]

# n= 9

# nums = [80, 20, 10, 60, 50, 70, 40, 30, 90]
dp = [1 for i in range(n)]


for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

max_dp = max(dp)

max_idx = dp.index(max_dp)

lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(nums[max_idx])
        max_dp -= 1
    
    max_idx -= 1
lis.reverse()

for i in lis:
    print(i, end = ' ')

nums.reverse()

dp = [1 for i in range(n)]


for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)


max_dp = max(dp)

max_idx = dp.index(max_dp)

lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(nums[max_idx])
        max_dp -= 1
    
    max_idx -= 1
print()
for i in lis:
    print(i, end = ' ')

sys.stdout.close()



# orders = []

# for i in range(1, max(dp)+1):
#     orders.append(dp.count(i))

# p =0
# answer = []
# for i in orders:
#     print(min(nums[p:p+i]), end = " ")
#     p += i


# for i in range(n):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(dp)

# for i in range(1,max(dp)+1):
#     mint = []
#     for j in range(0, n, dp.count(i)):
        
#         mint.append(j)
#     real.append(min(mint))

# print(real)

    # real.append()


# nums = [80, 20, 10, 60, 50, 70, 40, 30, 90]

# dp = [0 for i in range(n)]
# p = [0] * n
# m = [0] * (n+1)
# l = 0

# for i in range(n):
#     low = 1
#     high = l
#     while low <= high:
#         mid = (low + high) // 2
#         if (nums(m[mid]) < nums[i]):
#             low = mid + 1
        
#         else:
#             high = mid - 1
#     newl = low
#     p[i] = m[newl-1]
#     m[newl] = i

#     if newl > l:
#         l = newl
# print(p)
# print(m)
# print(l)

# print(newl)


# for i in range(l-1, -1, -1):
#     s.append(nums[k])
#     k = p[k]

# print(s[::-1])


# for i in range(l-1, -1, -1):
#     s.append(nums)

# print(p)

# print(dp)
        
# for i in dp:
#     print(nums[i], end = " ")
