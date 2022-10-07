from functools import total_ordering

@total_ordering
class Movie:
    
    # to protect attribute list
    __slots__ = ['title', 'year']
    
    # constructor
    def __init__(self, title=None, year=None):
        self.title = title
        self.year = year
        
    # __repr__ => ____str__
    def __repr__(self):
        return f"{self.title} ({self.year})"
    
    def __eq__(self, other):
        # strict typing (or isinstance)
        if type(other) != Movie:
            return NotImplemented
        return (self.title, self.year) == (other.title, other.year)
    
    def __hash__(self):
        # NB: None is False
        hash_title = hash(self.title) if self.title else 0
        hash_year = self.year if self.year is not None else 0
        return hash_title + hash_year
    
    def __lt__(self, other):
        if type(other) != Movie:
            return NotImplemented
        return (self.year, self.title) < (other.year, other.title)
    

