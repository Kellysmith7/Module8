"""
Program: dict_membership.py
Author: Kelly Smith
Last day updated: 10-12-19

Program to find an elemenet in a dictonary
:param
:return
"""


def in_dict(x):
    dict_pets = {"type": "cat", "size": "medium", "breed": "American Shorthair"}
    if x in dict_pets:
        return 'True'
    else:
        return 'False'


if __name__ == '__main__':
    print(in_dict("type"))

