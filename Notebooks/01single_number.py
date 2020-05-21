
# 0(n^2) solution


def single_number_with_array(nums):
    # first-pass solution
    # we'll keep an array, call it 'no_dups' to hold numbers we see in the nums array
    no_dups = []
    # iterate through nums

    # using an array to hold the dups and then searching through it
    # one thing that arrays are not great are is searching for a particular value
    # in the worst case, that's going to be 0(n)

    # what are other data structures that better suited to being searched?

    for x in nums:
        # check to see if the number is already in the 'no_dups' array
        if x not in no_dups:
            no_dups.append(x)
        # if it is, remove it from the 'no_dups' array
    else:
        no_dups.append(x)
        # when we're done iterating, the only number in our 'no_dups' array is the
        # odd number out
        # return it
        return no_dups[0]

# +------------------------------+
# 0(2 * n) ~ 0(n) solution


def single_number(nums):

    # keep track of the counts of how many times
    # we've seen a particular number
    #
    # dictionaries are better at being searched
    counts = {}

    # 0(n)
    # loop through nums to tally up how many times we've seen each number
    for x in nums:
        if x in counts:  # 0(n)
            counts[x] += 1
        else:
            counts[x] = 1
    # loop through all of the key-value pairs in counts to find the one pari
    # whose value is 1
    # 0(1)
    # this look will be looping through one entry
    for num in counts:
        if counts[num] == 1:
            return num
