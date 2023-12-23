"""
Practice with Python
jeje
"""
# for use colors in the console
from colorama import Fore, Style, init

# pants for use
PANTS = {
        'Levis': 10,
        'Acer': 1000,
        'Silver': 1000
    }

# n = 0

# changing values for get a errror
PANTS['Silver'] = 12.2
# PANTS['Acer'] = 34.5

# function
validate_price = lambda price: price <= 100

# funnction for get a list of numbers
get_list = lambda : [1, 2, 3]

def validate_len_list(list_v):
    """
    Return la longuitud los valores contenidos en la lista segun la
    condicion

    """

    # validating the longuited of list for return the value
    if len(list_v) == 2:
        # if falta 1
        return 1

    elif len(list_v) == 1:
        # si faltan 2
        return 2

    # if no falta ninguno
    return 3

# list for validate the validations
list_v = get_list()

if __name__ == '__main__':
    # for colorama jeje
    # init( autoreset = True )

    # for m in PANTS:
        # # validating the price of PANTS
        # v = validate_price( PANTS[m])

        # # if return True
        # if v:
            # print( Fore.LIGHTBLUE_EX + Style.DIM + 'Good Shop' )

        # else:
            # # removing a element
            # list_v.pop()
            # print( Fore.LIGHTCYAN_EX + Style.BRIGHT + 'Bad Shop' )

    # if validate_len_list(list_v) == 2:
        # print( Fore.LIGHTRED_EX + Style.BRIGHT + '\nTwo Bad.' )

    # elif validate_len_list(list_v) == 1:
        # print( Fore.LIGHTYELLOW_EX + Style.BRIGHT + '\nOne Bad.')

    # else:
        # print( Fore.GREEN + Style.BRIGHT + '\nAlls Good.' )


    # execute for get information about the list
    # print(len(list_v))

    import doctest
    doctest.testmod()
    'Silver'
