# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler006
#
# Problem
# =======
# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... 
# + 10^2 = 385. The square of the sum of the first ten natural numbers is 
# (1 + 2 + ... + 10)^2 = 55^2 = 30252. Hence the absolute difference between 
# the sum of the squares of the first ten natural numbers and the square of the
# sum is 3025 - 385 = 2640.
#
# Find the absolute difference between the sum of the squares of the first N
# natural numbers and the square of the sum.
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. This is followed 
# by T lines, each containing an integer, N.
#
# Constraints
# ============
# 1 <= T <= 10^4
# 1 <= N <= 10^4
#
# Output Format
# =============
# Print the required answer for each test case.

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    square_of_sum = ((n)*(n+1)/2)**2
    sum_of_squares = n*(n+1)*(2*n+1)/6
    print(int(square_of_sum-sum_of_squares))