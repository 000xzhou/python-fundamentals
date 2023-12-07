def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # get only the letter that's swaping
    # ???????????
    # swap
    x = list(phrase)
    for i, letter in enumerate(x):
        if letter == to_swap or letter == to_swap.swapcase():
            x[i] = letter.swapcase()
    return "".join(x)
    
print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))