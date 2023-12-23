"""
This is a program for do
task of mathematic
"""
# for use colors
from colorama import init
# for use functions
from utils_math import get_list, show_number, get_format


def imprime_numbers(repeat):
    """Imprime the numbers for the task"""

    # the VALUE begining in 0
    VALUE = 500

    # doing the while loop for show each number
    c = 0
    while c < repeat:
        # getting the list of digit for each number
        # le pasamos el valor pero en string
        list_n = get_list( str(VALUE) )

        # validando si aplicar el formateo de agregar la coma en el string o no
        if not len(list_n) > 3:
            # si el numero no es mayor a 30 no tiene sentido poner la coma
            show_number(list_n)
            print()

        else:
            get_format(list_n, ',')
            # showing the numbers
            show_number(list_n)
            print()

        # aumentando el valor a 500, para que en la segunda iteration
        # ya no sea 500, si no 1000, y asi
        VALUE += 500
        # aumentando el counter for the while loop
        c += 1


if __name__ == '__main__':
    init( autoreset = True )
    # executing the function for imprime the numbers
    imprime_numbers( 10 )
