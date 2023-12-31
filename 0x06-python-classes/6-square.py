#!/usr/bin/python3
""" Task 5 """


class Square:
    """This is a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        This is the square constructor
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        if isinstance(position, tuple) and len(position) == 2 \
                and isinstance(position[0], int) and isinstance(position[1], int) \
                and position[0] >= 0 and position[1] >= 0: 
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """
        Getter Function for the square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter Function for the square's size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Getter Function for the square's position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0 and isinstance(value[0], int) \
                    and isinstance(value[1], int):
                self.__position = value
            return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Function to return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """
        Function to print the square to stdout with "#"
        """
        if self.__size != 0:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(' ', end="")
                for _ in range(self.__size):
                    print('#', end="")
                print('')
        else:
            print('')
