#!/usr/bin/python3
class Square:
    """
    creates a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """
        initializes instance of a square
        Args:
            __size(int): size of square
            __position(tuple):position
        """
    @property
    def size(self):
        return self.__size
        """
        gets size
        """
    @property
    def position(self):
        return self.__position
        """
        gets position
        """
    @position.setter
    def position(self, value):
        if(type(value) is not tuple or len(value) is not 2 or value[0] < 0 or
           value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        """
        sets position
        position has to be a tuple of positive integers
        """
    @size.setter
    def size(self, value):
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        sets size
        size has to be an integer and positive
        """

    def area(self):
        return(self.__size**2)
        """
        returns the area of the size of the square
        """
    def my_print(self):
        if(self.position[1]):
            print('' * self.position[1])
        for x in range(self.size):
            if(self.position[0]):
                print(" " * self.position[0], end='')
            print("#" * self.size, end='')
            print()
        """
        prints a square of hashtags based on position and size
        """
    def __str__(self):
        if(self.size == 0):
            return ''
        newlines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = "#" * self.size
        return newlines + '\n'.join(spaces + hashes for x in range(self.size))
