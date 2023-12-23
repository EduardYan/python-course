"""
This is a test with a animation
with the function Cursor from colorama

"""

# for show colors in the console
from colorama import Cursor, Fore, Style, init
# for work with the time
from time import sleep


def get_animation(time_a):
    """
    Show a animation for the console
    """

    # style of animation
    STYLE_ANIMATION = Fore.LIGHTGREEN_EX + Style.DIM
    # list of element for show in loop
    LIST_ELEMENTS = [ '$----', '-$---', '--$--', '---$-', '----$', '-----' ]
    ULTI = '-------'

    # add the new element
    LIST_ELEMENTS.append( ULTI )


    # doing the for loop for show animacion
    for e in LIST_ELEMENTS:
        # # put the time
        sleep( time_a )
        ANIMATION = Cursor.POS( 37,3 ) + STYLE_ANIMATION + str(e)

        # print the ANIMATION
        print( ANIMATION )


    # with while loop (this forma es mas verbosa)
    # c = 0
    # while c < len( LIST_ELEMENTS ):
        # sleep( time_a )

        # ANIMATION = Cursor.POS( 37, 3 ) + STYLE_ANIMATION + str(LIST_ELEMENTS[c])

        # print(  ANIMATION )

        # c += 1


def main():
    """ Execute the code for animacion """

    des = input( 'Quieres ver la animacion?: ' )

    # validando la ejecucion
    if des == 'y'or des == 'yes':
        get_animation( 0.5 )


    elif des == 'n' or des == 'no':
        print( Fore.GREEN + Style.DIM + 'Not Show Animation.' )


    else:
        print( Fore.CYAN + Style.DIM + 'Elige alguna opcion.' )


if __name__ == '__main__':
    init( autoreset = True )
    # executing the main() function
    main()
