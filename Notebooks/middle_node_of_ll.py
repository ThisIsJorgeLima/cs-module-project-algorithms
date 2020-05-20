# Can we figure out the length of the ll? Yes
# what is a linked list?
# Will we always be given the head? Yes
# How do we traverse?
# How do we know when we've reached the end?
# Can we add more attributes to the class? To be safe: No
# Singly-linked or doubly-linked ll? Singly
# What's the target time complexity?
# Edge case: what do we do in the case of just two nodes?
# Is the list valid?

# +------------------------------+
# If we know the length of the ll, then we can calculate the middle "index" using
# a mid point formula, and then perform the appropriate number of jumps from the
# head to get the middle node
# +------------------------------+

# Can using two pointers/runners help us in this case?
# Idea: let's have one of the runners run twice as fast the other through the linked list
#
