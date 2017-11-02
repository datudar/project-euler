# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of a given number?

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