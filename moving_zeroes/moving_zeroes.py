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

# standup

# left = 0
# right = len(arr) - 1
#
# while left <= right:
#     if arr[left] == 0 and arr[right] != 0:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
#     else:
#         if arr[left] != 0:
#             left += 1
#         if arr[right] == 0:
#             right -= 1
#     return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
