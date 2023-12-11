def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    chars = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if chars[i].lower() not in vowels:
            i += 1
        if chars[j].lower() not in vowels:
            j -= 1
        if chars[i] in vowels and chars[j] in vowels:
            chars[i],chars[j] = chars[j],chars[i]
            i += 1
            j -= 1
    return "".join(chars)
            
    
assert reverse_vowels("Hello!") == 'Holle!'
assert reverse_vowels("Tomatoes") == 'Temotaos'
assert reverse_vowels("Reverse Vowels In A String") == 'RivArsI Vewols en e Streng'
assert reverse_vowels("aeiou") == 'uoiea'
assert reverse_vowels("why try, shy fly?") == 'why try, shy fly?'