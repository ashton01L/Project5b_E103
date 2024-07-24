# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/23/2024
# Description: Define a class named Taxicab that has three private
# data members: one that holds the current x-coordinate (x_coord)
# one that holds the current y-coordinate (y_coord)
# and one that holds the current odometer reading (odometer).

class Taxicab:
    """
    A class representing a Taxicab with coordinates and an odometer.

    Attributes:
        _x_coord: integer, Current x-coordinate of the Taxicab.
        _y_coord: integer, Current y-coordinate of the Taxicab.
        _odometer: integer, Current odometer reading of the Taxicab.

    Methods:
        __init__(self, x, y):
            Initializes a new Taxicab object with given coordinates and odometer set to zero.

        get_x_coord(self):
            Returns the current x-coordinate of the Taxicab.

        get_y_coord(self):
            Returns the current y-coordinate of the Taxicab.

        get_odometer(self):
            Returns the current odometer reading of the Taxicab.

        move_x(self, distance):
            Moves the Taxicab horizontally by the specified distance.

        move_y(self, distance):
            Moves the Taxicab vertically by the specified distance.
    """

    def __init__(self, x, y):
        """
        Initializes the Taxicab object with given parameters

        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        """
        self._x_coord = x
        self._y_coord = y
        self._odometer = 0

    def get_x_coord(self):
        """
        Returns the current x-coordinate of the Taxicab

        :param self: x-coordinate
        :return: integer, Current x-coordinate
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the current x-coordinate of the Taxicab

        :param self: y-coordinate
        :return: integer, Current y-coordinate
        """
        return self._y_coord

    def get_odometer(self):
        """
        Returns the current odometer reading of the Taxicab

        :param self: odometer
        :return: integer, Current odometer
        """
        return self._odometer

    def move_x(self, distance):
        """
        Moves the Taxicab horizontally along the x-coordinate plane,
            left (negative values) or right (positive values)

        :param self: measure of movement along x-coordinate
        :param distance: integer, Distance to move along the horizontal plane (x-coord)
        :return: no return
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Moves the Taxicab vertically along the y-coordinate plane,
            down (negative values) or up (positive values)

        :param self: measure of movement along y-coordinate
        :param distance: integer, Distance to move along the vertical plane (y-coord)
        :return: no return
        """
        self._y_coord += distance
        self._odometer += abs(distance)

# taxicab = Taxicab(1, -6)
# taxicab.move_x(-3)
# taxicab.move_y(5)
# taxicab.move_x(32)
# print(taxicab.get_odometer())                                               # should print 40
# print("(x:", taxicab.get_x_coord(), ", y:", taxicab.get_y_coord(), ")")     # should print (x: 30, y: -1)
