class Rectangle:
    def __init__(self, length: int, width: int):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers.")
        
        self.length = length
        self.width = width
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration

    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

# Example usage
try:
    rect = Rectangle(5, 10)  
    for attribute in rect:
        print(attribute)
except ValueError as e:
    print(e)

# Invalid rectangle example
try:
    invalid_rect = Rectangle(-2, 10)  
except ValueError as e:
    print(e)
