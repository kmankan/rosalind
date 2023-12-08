# Problem 4: Rabbits and Recurrence Relations
# https://rosalind.info/problems/fib/
# Return: 
# The total number of rabbit pairs that will be present after n months, 
# if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
# rabbit pairs (instead of only 1 pair).

"""
Working out the expression:
* n=1, r = 1  # start with 1 pair
* n=2, r = 1  # not mature enough to reproduce
* n=3, r = (n-1) + (n-2)*k = 1 + 3 = 4  # original pair is ready to reproduce (1*k)
* n=4, r = (n-1) + (n-2)*k = 4 + 1*3 = 7  # original pair reproduces again (1*k)
* n=5, r = (n-1) + (n-2)*k = 7 + 4*3 = 19 # original pair + next gen reproduce ((1+3)*k
* n=6, r = (n-1) + (n-2)*k = 19 + 7*3 = 40 # original pair + next + subsequent reproduce (1+3+3)*k
"""

# This is a modification of a normal recursion function with memoization to reduce memory
# i.e. Let's just remember all the results computed so far instead of recomputing them
def recurrence_relationship_of_rabbits(n, k = 1, memo = {}):
    # # Check if result is in the memoization dictionary, if it is return that instead of computing it
    if (n,k) in memo:
        return memo[(n,k)]
    
    # Base cases for first two months
    if n == 1 or n == 2:
        return 1

    else:
    # Recursive case: compute the value using the modified Fibonacci formula
    # F_n = F_(n-1) + k * F_(n-2)
    # where F_(n-1) is the number of rabbit pairs last month, and
    # k * F_(n-2) is the number of new rabbit pairs born this month
      ans = (recurrence_relationship_of_rabbits(n-1,k) + (k * recurrence_relationship_of_rabbits(n-2,k)) )
      # store the computed value for the nth month
      memo[(n,k)] = ans
      # return the answer
      return ans
    
print(recurrence_relationship_of_rabbits(5,3))