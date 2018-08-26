# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008
#
# Problem
# =======
# Find the greatest product of K consecutive digits in the N digit number.
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. 
# First line of each test case will contain two integers N & K. 
# Second line of each test case will contain a N digit integer.
#
# Constraints
# ============
# 1 <= T <= 100
# 1<= K <= 7
# K <= N <= 1000
#
# Output Format
# =============
# Print the required answer for each test case.

def product(num_subset):
    p = 1
    for i in num_subset:
        p *= i
    return p

t = int(input().strip())
for _ in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    p = []    
    for i in range(n-k):
        num_subset = [int(x) for x in list(num[i:k+i])]
        p.append(product(num_subset))
    print(max(p))