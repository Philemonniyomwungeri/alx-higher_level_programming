#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Defines a square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square."""
        s = ""
        if self.__size == 0:
            return s
        for _ in range(self.__position[1]):
            s += '\n'
        for _ in range(self.__size):
            s += " " * self.__position[0] + "#" * self.__size + '\n'
        return s[:-1]

# Test the Square class with examples
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
