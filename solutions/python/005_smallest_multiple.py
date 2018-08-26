# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005
#
# Problem
# =======
# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder. 
#
# What is the smallest positive number that is evenly divisible (divisible with
# no remainder) by all of the numbers from 1 to N?
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. This is followed 
# by T lines, each containing an integer, N.
#
# Constraints
# ============
# 1 <= T <= 10
# 1 <= N <= 40
#
# Output Format
# =============
# Print the required answer for each test case.

from functools import reduce

def greatest_common_factor(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    n = int(input())
    print(reduce(lambda x, y: x * y // greatest_common_factor(x, y), range(1, n+1)))
