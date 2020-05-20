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
