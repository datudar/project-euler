# Problem
# ======= 
# A palindromic number reads the same both ways. The smallest 6 digit 
# palindrome made from the product of two 3-digit numbers is 
# 101101 = 143 x 707. 
#
# Find the largest palindrome made from the product of two 3-digit numbers 
# which is less than N.
#
# Input Format
# ============
# First line contains T that denotes the number of test cases. This is followed
# by T lines, each containing an integer, N.
#
# Constraints
# ===========
# 1 <= T <= 100
# 101101 < N < 1000000
#
# Output Format
# =============
# Print the required answer for each test case in a new line.

def is_palindrome(n):
    return str(n) == str(n)[::-1]
    
def get_product(n):    
    for i in range(100,1000):
        for j in range(110,1000,11):
            if i*j == n:
                return i*j
    else:
        return None

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    n=n-1
    while True:
        if is_palindrome(n) == True:
            product = get_product(n)
            if product != None:
                print(product)
                break
            else:
                n -= 1
        else:
            n -= 1
