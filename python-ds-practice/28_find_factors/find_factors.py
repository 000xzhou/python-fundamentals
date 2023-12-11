def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = set()
    for i in range(1, num+1):
        if num % i == 0:
            if i not in factors:
                factors.add(i)
    return sorted(factors)
    
assert find_factors(10) == [1, 2, 5, 10]
assert find_factors(11) == [1, 11]
assert find_factors(111) == [1, 3, 37, 111]
assert find_factors(321421) == [1, 293, 1097, 321421]