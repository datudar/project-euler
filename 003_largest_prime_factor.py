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
# 10 <= N <= 10^2
#
# Output Format
# =============
# For each test case, display the largest prime factor of .
#
# Note: This solution receives 80 out of 100 points since it
# times out on the last test case.

def prime_factors(n):
    prime_factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            prime_factors.append(d)
            n = n / d
        d = d + 1
    return prime_factors

t = int(input())

for _ in range(t):
    n = int(input())
    print(max(prime_factors(n)))