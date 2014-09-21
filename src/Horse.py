#!/usr/bin/env python
# -*-coding:utf-8-*-

#############################################################
# Python Program - Horse.py
#
# project	: le-tock
# @authors	: Guillaume Josserand - Pierre Vrot
# @date		: 2014-09-21
#
#############################################################

#############################################################
# CLASS


class Horse:

    """
            This class describes a player by :
            - his number
            - his color
            - his coordonates on "x" (1 = 1*size_case)
            - his coordonates on "y" (1 = 1*size_case)

            This class >>>WILL<<< have methods :
    """
    # TODO

    ### CLASS CONSTRUCTOR ###################################

    def __init__(self, number, color, coord_x, coord_y):
        """ Constructor of one Horse """
        self._number = number
        self._color = color
        self._coord_x = coord_x
        self._coord_y = coord_y

    ### GETTERS/SETTERS #####################################
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def coord_x(self):
        return self._coord_x

    @coord_x.setter
    def coord_x(self, value):
        self._coord_x = value

    @property
    def coord_y(self):
        return self._coord_y

    @coord_y.setter
    def coord_y(self, value):
        self._coord_y = value
