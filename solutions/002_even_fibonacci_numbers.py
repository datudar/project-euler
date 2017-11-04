# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002
#
# Problem
# =======
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not
# exceed N, find the sum of the even-valued terms.
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. This is 
# followed by T lines, each containing an integer, N.
#
# Constraints
# ===========
# 1 <= T <= 10^5
# 10 <= N <= 4 x 10^16
#
# Output Format
# =============
# Print the required answer for each test case.

def even_fibo(n):
    num1, num2 = 0, 1
    fibo_arr = []
    while num2 < n:
        num1, num2 = num2, num1+num2
        fibo_arr.append(num1)
    return [n for n in fibo_arr[:] if n % 2 == 0]

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(sum(even_fibo(n)))