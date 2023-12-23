"""
Working with lineals functions

"""

# for use colors
from colorama import Fore, Style, init

# def get_value(v):
    # """ Return the value with your logaritme """
    # # return the result
    # return v * -2 + 3

# Return the value with your logaritme
get_value = lambda v : v * -2 + 3

def show_value(v, v_x):
    """ Show the value of function """
    # geting the value of the sucession
    value = get_value(v)

    # style for show
    STYLE_SHOW = Fore.LIGHTCYAN_EX + Style.DIM

    # format for show
    format_shower = STYLE_SHOW + f'y => {value}'
    # showing the format
    print( format_shower )


# sucession for variar the number
SUCESSION = ( -3, -2, -1, 0, 1, 2, 3 )

if __name__ == '__main__':
    init(autoreset = True)
    # recorriendo la sucession
    for n in SUCESSION:
        # showing the x value
        print( f'x => {n}' )
        show_value(n, SUCESSION)
        print( '------------------' )
