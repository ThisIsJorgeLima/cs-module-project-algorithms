def eating_cookies(n):
    """
call this recursively:
with n-1
 represents Cookie Monster eating one cookie:
eating_cookies(n-1)
 represents Cookie Monster eating two cookies:
eating_cookies(n-2)
represents Cookie Monster eating three cookies:
     eating_cookies(n-3)
    """
    # <------------------ LECTURE----------------------->
    # <------------------CODEBASE---------------------->
    # <--------------------BELOW------------------------->
    # <--------------------VVVVV------------------------->
    # <---------------------VVVV-------------------------->
    # <----------------------VVV--------------------------->
    # <------------------------V------------------------------>

    """
    Caching/ memoization: Let's save our work so we don't have
    to recompute it agan.

    - Need some sort of data structure where we'll save the data
    - arrays and dictionaries
    - If we check our cache and see that the answer we're looking for
    - is already in there, just return that answer
    - do we get answers in there?
    - There's going to be a first time for calculating an answer, and we're going to do it the same way we're currently doing it
    """

    #  base case: when there are no more cookies
    if n == 0:
        return 1
    #
    #  lets check for negative n values
    elif n < 0:
        return 0

    # init our cache if we don't have it yet
    # add a case to have us check the cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # cache = {i: 0 for i in range(n+1)}
            # return cache[n]
            cache = [0 for _ in range(n+1)]
            # we can go ahead and save our answer to the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2,
                                                               cache) + eating_cookies(n-3, cache)
        return cache[n]


    #  this represents our recursive case where
    #  there still some cookies to be eaten
    # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    # print(eating_cookies(5))
print(eating_cookies(999))
"""
        Here's another explanation of why we're adding three recursive calls:
    """

# the number of ways to eat n cookies (at most 3 at a time) is equal to...
# the number of ways to first eat 3 cookies at once right now + and then eat the remaining cookies later
# ways_if_3_cookies_eaten_first = eating_cookies_unoptimized(n - 3)
# the number of ways to first eat 2 cookies at once right now + and then eat the remaining cookies later
# ways_if_2_cookies_eaten_first = eating_cookies_unoptimized(n - 2)
# the number of ways to first eat a single cookie right now + and then eat the remaining cookies later
# ways_if_1_cookie_eaten_first = eating_cookies_unoptimized(n - 1)
# return ways_if_3_cookies_eaten_first + ways_if_2_cookies_eaten_first + ways_if_1_cookie_eaten_first

if __name__ == "__main__":
        # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
