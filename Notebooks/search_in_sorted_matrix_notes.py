# How do we traverse a matrix?
# Are nested loops acceptable?
# Would be backtracking/recursion be useful for this?
# Can be target be negative?
# How do we take advantage of the fact the matrix is sorted?
# Can subarrays contain arrays themselves? No
# Can binary search help us?

# Can we solve an easier version of the problem first?
# Change the problem to just be searching in a matrix?

matrix = [[]]

# row indices
for i in range(len(matrix)):
    # column indices
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            return [i, j]


# iterate along the rows
for row in matrix:
    # iterate along the columns
    for elem in row:
        if elem == target:
