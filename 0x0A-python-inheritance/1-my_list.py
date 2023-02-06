#!/usr/bin/python3
""" New Class """


class Mylist(list):
    """ Mylist class that inherit from list """

    def print_sorted(self):
        """ Function that prints a sorted list """
        print(sorted(self))
