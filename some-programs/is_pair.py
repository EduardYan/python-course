"""
This program is util for verify if a number
is pair or not

"""


def is_pair(n):
    """
    Return True or False segun the condition
    of n recibe
    """
    if type(n) not in [int, float]:
        raise ValueError("El valor recibido no es un int o un float.")

    if n % 2 != 0:
        return False

    return True


def get_lists():
    """Return lists"""
    return [], []


list_pair, list_inpair = get_lists()

if __name__ == '__main__':
    print("Enter Numbers witout spaces.For verify.")

    while True:
        try:
            # getting values
            n = input( 'Number to Verify: ' )

            if n == 'e':
            :q
                break

            else:
                # validating if is pair
                if is_pair( float(n) ):
                    list_pair.append( float(n) )
                    print( 'The number is pair.' )

                else:
                    list_inpair.append( float(n) )
                    print( 'The number is inpair.' )

                for number_p in list_pair:
                    print("Pairs")
                    print(f"The number {number_p} is pair.")

                for number_in in list_inpair:
                    print("Inpairs")
                    print(f"The number {number_in} is inpair")

                list_pair.clear()
                list_inpair.clear()

        except ValueError:
            print( 'Enter Numeric Values.' )

    print( 'Exited:)' )
