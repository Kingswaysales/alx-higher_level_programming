#!/usr/bin/python3
""" New Class """


class Mylist(list):
    """ class my_list """
    def print_sorted(self):
        """ method to print """
        print(sorted(self))
