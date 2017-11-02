# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below N.

def calc_sum(n, multiple):
    num_of_multiples = (n - 1) // multiple
    return multiple * (num_of_multiples * (num_of_multiples + 1)) // 2

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    
    sum_3 = calc_sum(n, 3)
    sum_5 = calc_sum(n, 5)
    sum_15 = calc_sum(n, 15)
  
    print(sum_3 + sum_5 - sum_15)