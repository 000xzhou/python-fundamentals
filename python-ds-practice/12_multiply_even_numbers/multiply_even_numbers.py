def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even_num = []
    for num in nums:
        if num%2 == 0:
            even_num.append(num)
    sum = 1
    if not even_num:
        return 1
    else:
        for num in even_num:
            sum *= num
    return sum
