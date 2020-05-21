# Example: find 5!
# 5! = Fice factorial = 1*2*3*4*5 = 120

"""
🄽🄾🅃🄴🅂:
Notes: 0! = 1
            1! = 1

Let's find an algorithm to find factorial for any number: n!

!n 🄸🅃🄴🅁🄰🅃🄸🅅🄴 algorithm= Looping
- The iterative solution uses a loop, and computes as it goes.

e.g., simple algo
function getFactorial(5) --> get integer 5
    factorial = 1  ---> Our running total
    for x = 1 to 5 ---> A loop that runs 1-5
        factorial = factorial*x ---> multiple numbers 1-5 * are running time factorial.
        e.g., it will multiple by 2 then * 3 then *4 then * 5 then ext.

+--------------------------------------------------------------+
A 🅁🄴🄲🅄🅁🅂🄸🅅🄴 Algorithm:

A recursive function breaks the problem down into smaller problems, and calls itself for each of the smaller problems.

It includes a base case(or terminal case) and a recursive case.

e.g., 5! = 5*4*3*2*1
            = 5*4
        4! = 4*3*2*1
            = 4*3!
        3! = 3*2*1
            = 3*2
        2! = 2*1
            = 1
        Base Cases:
        0! = 1
        1! = 1

+--------------------------------------------------------------+
🄵🅄🄽🄲🅃🄸🄾🄽 Calls:
getFactorial(5)                     5 * getFactorial(4)
        getFactorial(4)                 4 * getFactorial(3)
            getFactorial(3)                     3 * getFactorial(2)
                getFactorial(2)                         2 * getFactorial(1)
                    getFactorial(1)                             return 1
+--------------------------------------------------------------+
 🄵🅄🄽🄲🅃🄸🄾🄽
 function getFactorial(n)
    if n < 2, return 1
    else return n* getFactorial(n-1)
+--------------------------------------------------------------+
Recursion Pros: in some cases, extremely fast and easy to code.
Extremely practical for tree traversals and binary search.
"""

"""
🅁🄴🄲🅄🅁🅂🄸🅅🄴
"""

# excepts an interger of n


def get_recursive_factorial(n):
    # error check
    if n < 0:
        return -1
    # test for our base case:
    elif n < 2:
        return 1
    # recursive case n*get_recursive_factorial
    else:
        return n * get_recursive_factorial(n-1)


"""
🄸🅃🄴🅁🄰🅃🄸🅅🄴
"""

# excepts an interger of n


def get_iterative_factorial(n):
    # error check
    if n < 0:
        return -1
    else:
        # set our factorial counter set to one
        # to initialize it
        fact = 1
        # we start our loop:
        for i in range(1, n+1):
            # multiply fact by i
            fact *= i
            # return value
        return fact


"""
🅁🄴🄲🅄🅁🅂🄸🅅🄴
"""

print(get_recursive_factorial(6))
print(get_iterative_factorial(6))
