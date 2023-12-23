"""
This is a test with functions lambda
"""

# this is a lambda function
# add = lambda n1, n2 : n1 + n2


def add_2(n1, n2):
    """Return the add of n1 and n2"""
    if type(n1) not in [int, float]:
        raise TypeError(f"The value {n1} for parameter not is a int or a float.")

    if type(n2) not in [int, float]:
        raise TypeError(f"The value {n2} for parameter not is a int or a float.")

    return n1 + n2


if __name__ == '__main__':
    while True:
        try:
            n = float( input('Numero 1: ') )
            n_2 = float( input('Numero 2: ') )

            try:
                result = add_2( n, n_2 )
                print(result)

            except TypeError as e:
                print(e)

        # capturando el except, si los valores no son correctos
        except ValueError:
            print( 'Enter Numeric Values.' )
