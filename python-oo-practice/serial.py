"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.init = start
    
    def __repr__(self) -> str:
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"
        
        
    def generate(self):
        print(self.start)
        self.start += 1
    
    def reset(self):
        self.start = self.init

import doctest
doctest.testmod()

test = SerialGenerator(100)
print(test)