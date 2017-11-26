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

def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

t = int(input().strip())

for _ in range(t):

    primes = []
    count = 0
    num = 2

    n = int(input().strip())
    while count != n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    
    print(primes[count-1])