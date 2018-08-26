# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
#
# Problem
# =======
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below N.
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. This is followed
# by T lines, each containing an integer, N.
#
# Constraints
# ===========
# 1 <= T <= 10^5
# 1 <= N <= 10^9
#
# Output Format
# =============
# For each test case, print an integer that denotes the sum of all the 
# multiples of 3 or 5 below N.

def calc_sum(n, multiple):
    num_of_multiples = (n - 1) // multiple
    return multiple * (num_of_multiples * (num_of_multiples + 1)) // 2

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    
    sum_3 = calc_sum(n, 3)
    sum_5 = calc_sum(n, 5)
    sum_15 = calc_sum(n, 15)
  
    print(sum_3 + sum_5 - sum_15)