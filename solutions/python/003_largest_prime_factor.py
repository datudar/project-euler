# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler003
#
# Problem
# =======
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of a given number?
#
# Input Format
# ============
# First line contains T, the number of test cases. This is followed by T lines
# each containing an integer N.
#
# Constraints
# ===========
# 1 <= T <= 10
# 10 <= N <= 10^12
#
# Output Format
# =============
# For each test case, display the largest prime factor of N.

def prime_factors(n):
    prime_factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            prime_factors.append(d)
            n = n / d
        d = d + 1
        if d**2 > n:
            if n > 1:
                prime_factors.append(n)
            break
    return prime_factors


t = int(input())

for _ in range(t):
    n = int(input())
    print(int(max(prime_factors(n))))