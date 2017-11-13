# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007
#
# Problem
# =======
# By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that 
# the 6th prime is 13. 
#
# What is the Nth prime number?
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. This is followed 
# by T lines, each containing an integer, N.
#
# Constraints
# ============
# 1 <= T <= 10^3
# 1 <= N <= 10^4
#
# Output Format
# =============
# Print the required answer for each test case.

import math

t = int(input().strip())

primes = [2,3]

for _ in range(t):
    n = int(input())
    if len(primes) < n:
        x = primes[len(primes)-1]
        while len(primes) < n:
            x += 2
            y = math.floor(x**0.5)
            count = 0
            for i in primes:
                if i > y:
                    count = 0
                    break
                if x % i == 0:
                    count = 1
                    break
            if count == 0:
                primes.append(x)

    print(primes[n-1])