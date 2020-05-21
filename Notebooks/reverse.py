"""
🄿🅁🄰🄲🅃🄸🄲🄴
So, we now undertand our recursive case and our base case. We now need to turn that into actual Python code. For our recursive case, where we are stating reverse("LAMBDA") = reverse("AMBDA") + "L", we can state this in general terms as reverse(str) = reverse(str[1:]) + str[0]. And we can check for an empty string for our base case with len(str) == 0.

"""


def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]

# + --------------------------+


def is_palindrome(str):
    # If the string is of length 0 or 1, it is a palindrome.
    if len(str) <= 1:
        return True
    # Otherwise, compare the first and last characters.
    if str[0] == str[-1]:
        # If the first and last characters are equal, strip those characters and check if the remaining characters are a palindrome.
        return is_palindrome(str[1:-1])
    return False

# + --------------------------+


def merge_sort(arr):
    if len(arr) > 1:
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
        pass
        # + --------------------------+


def merge_helper(a, b):
    merged_arr = []

    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    return merged_arr
