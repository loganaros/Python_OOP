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
        """Create a new generator, starting value is start"""
        
        self.next = start
        self.start = start

    def generate(self):
        """Returns next value"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets value to start value"""

        self.next = self.start
