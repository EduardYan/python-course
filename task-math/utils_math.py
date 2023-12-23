"""
This module have utils functions for use in
task_math.py
"""

# for show a style for numbers to show
from colorama import Fore, Style

# ---- styles ------
STYLE_OF_NUMBER = Fore.LIGHTGREEN_EX + Style.BRIGHT


def get_list(string):
    """
    Return a list with each element of the
    string recived
    """
    # returning the list
    return [n for n in string]


def get_format(list_e, sign):
    """
    Add a sign to the list of digits
    of number
    """
    # add a comma in the begin of list
    list_e.insert( 1, sign )

    return list_e


def show_number(list_n):
    """
    Show the number in the list
    Recive the list of digits from number
    """
    # showing the numbers with the format do
    for n in list_n:
        print(STYLE_OF_NUMBER + n, end = '')


if __name__ == '__main__':
    help(get_list)
    help(get_format)
    help(show_number)
