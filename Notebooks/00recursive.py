"""
To understand recursion,
you must first understand 𝘀𝘁𝗮𝗰𝗸𝘀.

A 𝘀𝘁𝗮𝗰𝗸 is a 𝗱𝗮𝘁𝗮 𝘀𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲 that holds a
squence of data and only lets you interact with
topmost item.

𝗙𝗶𝗿𝘀𝘁-𝗜𝗻, 𝗟𝗮𝘀𝘁-𝗢𝘂𝘁 (𝗙𝗜𝗟𝗢)

Tw̲o̲ m̲a̲i̲n̲ o̲p̲e̲r̲a̲t̲i̲o̲n̲s̲:̲
- Adding to the top of the stack is called 𝗽𝘂𝘀𝗵𝗶𝗻𝗴.
- Removing from the top of the stack is called 𝗽𝗼𝗽𝗽𝗶𝗻𝗴.

Python's lists are a stack if you only use 𝗮𝗽𝗽𝗲𝗻𝗱() and 𝗽𝗼𝗽()

e.g,

🄴🅇🄰🄼🄿🄻🄴 1.
>>> spam = []
>>> spam.append('Alice')
>>> spam.append('Bob')
>>> spam.append('Carol')
>>> spam.pop()
'Carol'
>>> spam
['Alice', Bob]

+-------------------------+
🄴🅇🄰🄼🄿🄻🄴 2.
"""

# functions calling functions:


def a():
    print('Start of a ()')
    b()
    print('End of a () ')


def b():
    print('Start of b ()')
    c()
    print('End of b')


def c():
    print('Start of c ()')
    print('End of c')


a()
print('+------------------+')
"""
The "call stack" is a stack of "frame objects".
        (frame object == a function call)

Recursion is a lot easier to understand if you
understand stacks and the call stack

Extra Credit:
Look up the inspect and traceback modules.
Doug Hellman's "Python Module of the Week" blog:

https://pymotw.com/3/inspect/
https://pymotw.com/3/traceback/
"""

"""
Factorial => *a terrible thing to use with recursion
factorial is a really simple math concept five factorial is:
5! = 5 x 4 x 3 x 2 x 1 = 120
2! = 2 x 1 = 2
4! = 4 x 3 x 2 x 1 = 24

Number! = Number x (Number -1)!
(Factorial has a recursive nature.)


A stack overflow is when a recursive function
gets out of control and doesn't stop recursing

🄴🅇🄰🄼🄿🄻🄴 1.
def factorial(number):
    return number * factorial(number - 1)


print(factorial(5))

+-----------------------+
Python actually has a built-in limit of 1,000 function calls
that you can make without returning.

"""
# hint: 1! = 1

# 5 x 4 x 3 x 2 x 1
# REMEMBER:
# The "call stack" is a stack of "frame objects".
#             (frame object == a function call)


def factorial(number):
    if number == 1:
        return 1  # BASE CASE

    # RECURSIVE CASE
    return number * factorial(number - 1)


"""
Your recursive function must always have at least
one base case and one recursive.

🄽🄾🅃🄴:
 It'll keep recursing forever and cause a stack overflow
 and you need to have at least on recursive case becuase
 otherwise it's not a recursive function if it doesn't call itself.

 *When your writing code for recursion it's a great
 starting point to just think what's my base case and
 what's my recursive case and make sure that your
 recursive case eventually hits one of the base cases.
 +----------L̲O̲O̲K̲ A̲T̲ E̲X̲A̲M̲P̲L̲E̲ A̲B̲O̲V̲E̲-----------+
"""


print('Factorial:')
print(factorial(5))
