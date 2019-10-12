"""
Program: set_membership.py
Author: Kelly Smith
Last day updated: 10-12-19

Program to determine if a color is in the set

:param kelly_set: set of colors
:return True or False if a color is in the set
"""


def in_set(x):
    kelly_set = {'red', 'blue', 'green', 'yellow'}
    if x in kelly_set:
        return 'True'
    else:
        return 'False'


if __name__ == '__main__':
    print(in_set('red'))
