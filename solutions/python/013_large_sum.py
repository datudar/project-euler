# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler013
#
# Problem
# =======
# Work out the first ten digits of the sum of N*50 digit numbers.
# 
# Input Format
# ============
# First line contains N; next N lines contain a 50 digit number each.
#
# Constraints
# ===========
# 1 <= N <= 10^3
#
# Output Format
# =============
# Print only first 10 digit of the final sum.

numbers = []

for _ in range(int(input())):
    numbers.append(int(input()))
    
print(str(sum(numbers))[:10])