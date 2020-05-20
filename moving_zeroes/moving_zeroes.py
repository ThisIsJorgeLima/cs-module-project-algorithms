'''
Input: a List of integers
Returns: a List of integers
'''

# our current arr  is 0,3,1,0,-2


def moving_zeroes(arr):
    zeros__at_end = 0
    while zeros__at_end < len(arr):
        if max(arr[zeros__at_end:]) == 0 and min(arr[zeros__at_end:]) == 0:
            break  # if so lets stop our loop
        if arr[zeros__at_end] == 0:
            arr.append(arr.pop(zeros__at_end))

        zeros__at_end += 1
        # return value:
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
