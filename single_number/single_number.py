'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # sort the array
    arr.sort()
    # allocate space
    # check and see if number isn' there

    # look for a skip in pairs
    for i in range(0, len(arr), 2):  # go by twos
        # checking the value at the end
        # eleven values 0-10
        if i == len(arr) - 1:  # last index
            arr[i]
        else:  # or
            if arr[i] is not arr[i + 1]:
                # reach the end
                return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr is always going to be odd number
    # IndexError: list index out of range
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
