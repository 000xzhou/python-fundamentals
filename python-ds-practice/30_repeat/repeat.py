def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if isinstance(num, int) and num >= 0:
        return phrase * num
    else:
        return None

assert repeat('*', 3) == '***'

assert repeat('abc', 2) == 'abcabc'

assert repeat('abc', 0) == ''

assert repeat('abc', -1) is None 

assert repeat('abc', 'nope') is None 