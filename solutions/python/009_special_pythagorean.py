# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler009
#
# Problem
# =======
# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# Given N, check if there exists any Pythagorean triplet for which
# a + b + c = N. Find the maximum possible value of a*b*c among all such 
# Pythagorean triplets. If there is no such Pythagorean triplet, print -1.
#
# Input Format
# ============
# The first line contains an integer T, i.e. number of test cases. 
# The next T lines will contain an integer N.
#
# Constraints
# ============
# 1 <= T <= 3000
# 1 <= N <= 3000
#
# Output Format
# =============
# Print the value corresponding to each test case in separate lines.   

t = int(input())

for i in range(t):
    n = int(input())
    arr = [-1]
    if n >= 12:
        for a in range(3, n//3):
            b = int((n*n - 2*n*a)/(2*n - 2*a))
            c = n - a - b
            if (a**2 + b**2) == c**2:
                product = a*b*c
                arr.append(product)
    print(max(arr))