"""
This is a test with sets
"""

options = {'yes', 'y', 'no', 'n'}
# convirtiendo el set de options to a tuple
new_options = tuple(options)

class Hola:
    def __init__(self):
        print( 'hola' )


if __name__ == '__main__':
    des = input('Yes Or No [y][n]: ')

    greeting = Hola()

    if des == new_options[0] or des == new_options[1]:
        print('yes')

    elif des == new_options[2] or des == new_options[3]:
        print('not')

    else:
        print('choice a option')


# doing some tests
# name = ('Ana',)

# if isinstance(name, str):
    # print('es un string')

# else:
    # print('no es un string')
