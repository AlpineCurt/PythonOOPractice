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
        self.num = start - 1
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next = {self.num + 1}>"
    
    def generate(self):
        """returns the next number in sequence"""
        self.num += 1
        return self.num
    
    def reset(self):
        """Resets the sequence to the initial value when it was created"""
        self.num = self.start - 1
