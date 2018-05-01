#!/usr/bin/python3
"""
import math class magic class
"""
import math


class MagicClass:
    """
    class magicclass initialized
    """
    def __init__(self, radius=0):
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius
        """
        initializes
        """
    def area(self):
        return self._MagicClass__radius ** 2 * math.pi
        """
        gets area
        """
    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
        """
        gets circumference
        """
if __name__ == "__main__":
    import dis
    dis.dis(MagicClass)
