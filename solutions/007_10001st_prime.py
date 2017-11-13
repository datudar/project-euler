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