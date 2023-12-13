from random import shuffle
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Prints out random word from file
    
    >>> randomgen = WordFinder()
    
    >>> randomgen.total()
    7 words in file
    
    >>> randomgen.random()
    
    >>> randomgen.total()
    6 words in file
    
    >>> randomgen.countWord()
    1 words read so far
    
    """
    def __init__(self) -> None:
        with open(r"python-oo-practice\words.txt") as file:
            self.words = file.readlines()
            shuffle(self.words)
                
        self.count = 0
            
    def random(self):
        word = self.words.pop().rstrip()
        self.count += 1
        print(word)
        
    def countWord(self):
        print(f"{self.count} words read so far")
    
    def total(self):
        print(f"{len(self.words)} words in file")
        
class SpecialWordFinder(WordFinder):
    """Prints out random word from file while ignoring empty lines and comments 
    
    >>> SpecialWordFinder = WordFinder()
    
    >>> randomgen.random()
    
    >>> randomgen.countWord()
    1 words read so far
    
    """
    def random(self):
        word = self.words.pop().rstrip()
        while word == "" or word[0] == "#":
            word = self.words.pop().rstrip()
        self.count += 1
        print(word)