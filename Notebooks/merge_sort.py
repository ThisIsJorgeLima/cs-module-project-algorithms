def merge(A, B):
    # init the combined list that will hold the sorted elements from both A and B
    # combined = [0] * (len(A) + len(B))
    # combined = [0 for _ in range(len(A) + len(B))]
    combined = []

    # init the two pointers that start at each list
    a = 0
    b = 0

    while a < len(A) and b < len(B):
        # compare the elements that a and b point at
        if A[a] < B[b]:
            combined.append(A[a])
            a += 1
        else:
            combined.append(B[b])
            b += 1

    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list
    while a < len(A):
        combined.append(A[a])
        a += 1
    while b < len(B):
        combined.append(B[b])
        b += 1

    return combined


def merge_sort(arr):
    # break the array down recursively
    # base case: when the lists get down to lengths of 1
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr

# +----------------------------------------------+
# optimizing space *****
# UPER Model
# UNP and go back and write the code
# Final step is optimization


def merge_in_place(arr, start, mid, end):
    # left_array = arr[start:mid]
    # right_array = arr[mid:end]

    start_two = mid + 1

    if arr[mid] <= arr[start_two]:
        return arr  # its already merged
# set up our two pointers
    while start <= mid and start_two <= end:
        if arr[start] <= arr[start_two]:  # punctionation
            start = + 1  # increment start
        else:
            value = arr[start_two]
            index = start_two

        # shift all of the elements
        # set the index minus 1 shifts to the right

            while index != start:  # != is not equal too
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # update all of our pointers
            # increment start
            start += 1
            # increment mid
            mid += 1
            # increment start_two
            start_two += 1

    return arr

# +----------------------------------------------+

    # index


def merge_sort_in_place(arr, left, right):

    if right - left > 1:

        mid = (left+right)//2
        # recursive
        merge_sort_in_place(arr, left, mid)
        merge_sort_in_place(arr, mid+1, right)
        merge_in_place(arr, left, mid, right)

    return arr

    arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    merge_sort_in_place(arr,  0, len(arr))
    print(arr)
