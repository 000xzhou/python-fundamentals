from collections import Counter

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return Counter(str(num1)) == Counter(str(num2))

assert same_frequency(551122, 221515) == True
        
assert same_frequency(321142, 3212215) == False
        
assert same_frequency(1212, 2211) == True