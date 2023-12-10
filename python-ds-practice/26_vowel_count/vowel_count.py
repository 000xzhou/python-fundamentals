def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {}
    for i in phrase:
        if i.lower() in ('a', 'e', 'i', 'o', 'u'):
            if vowels.get(i.lower()):
                vowels[i.lower()] += 1
            else:
                vowels[i.lower()] = 1
    return vowels

assert vowel_count('rithm school') == {'i': 1, 'o': 2}
assert vowel_count('HOW ARE YOU? i am great!') == {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}