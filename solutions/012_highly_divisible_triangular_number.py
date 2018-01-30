# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler012
#
# Problem
# =======
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over N divisors?
#
# Input Format
# ============
# First line contains T, the number of test cases. Each test case consist of N
# in one line.
#
# Constraints
# ===========
# 1 <= T <= 10
# 1 <= N <= 103
#
# Output Format
# =============
# For each test case, print the required answer in one line.

def num_of_divisors(n):
    num = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            num += 2
        if i * i == n:
            num -= 1
    return num
    
triangular_number = [1]
divisor = [1]

for i in range(2, 100000): 
    triangular_number.append(int(i * (i + 1) / 2))
    if i % 2 == 0:
        divisor.append(int(num_of_divisors(i / 2) * num_of_divisors(i + 1)))
    else:
        divisor.append(int(num_of_divisors(i) * num_of_divisors((i + 1) / 2)))

for t in range(int(input())):
    n = int(input())
    for i in range(len(triangular_number)):
        if n < divisor[i]:
            print(triangular_number[i])
            break