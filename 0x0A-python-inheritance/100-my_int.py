#!/usr/bin/python3
""" New class """


class Myint(int):
    """ My int inherits from int """
    def __eq__(self, num):
        """ function for equals """
        return(int(self) != int(num))

    def __ne__(self, num):
        """ Function for not equals """
        return (int(self) == int(num))
