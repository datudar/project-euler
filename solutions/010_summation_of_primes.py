# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler010
#
# Problem
# =======
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes not greater than given N.
#
# Input Format
# ============
# First line contains an integer T, i.e. number of test cases.
# The next T lines will contain an integer N.
#
# Constraints
# ============
# 1 <= T <= 10^4
# 1 <= N <= 10^6
#
# Output Format
# =============
# Print the value corresponding to each test case in a separate line.

def is_prime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    primes = []
    for num in range(2,n+1):

        if is_prime(num):
            primes.append(num)

    print(sum(primes))