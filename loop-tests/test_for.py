"""
This is a test with loops
"""

# for use colors
from colorama import Fore, Style, init



# jeje
'''
for i in range(4):
    for j in range(4 - i):
        j += 1
        print(j + i, end = "")

    print()
'''

STYLE_ONE = Fore.BLUE
STYLE_TWO = Fore.GREEN
STYLE_THREE = Fore.RED
STYLE_FOUR = Fore.CYAN

init(autoreset = True)

def imprime_patron(sign):
    """
    Imprime a patron, with a style
    and a sign for parameter

    """
    c = 0
    while c <= 12:
        # print(style + sign, end = '')
        print( type(sign) )
        print(sign, end = '')

        c += 1

    print()

# imprime_patron(style_one, '/ ')
# imprime_patron(style_two, '/ ')
# imprime_patron(style_three, '/ ')
# imprime_patron(style_four, '/ ')
print(str(Fore.GREEN))
