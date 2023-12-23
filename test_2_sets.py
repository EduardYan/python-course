"""
Test with sets
jeje
"""

def validate_name(name : str, data : set):
    """
    Validate a name in a conjunt of data
    """
    if not isinstance(data, set) and not isinstance(data, list):
        # provocando el except
        raise TypeError( "The values not are sets or tuples." )

    else:
        # validating
        if not name in data:
            return 1

        return 0

# lists
list_n = ['Ana', 'Ramiro']
list_n_2 = ['Carlos', 'Fabia']


# sets
names = { 'Ana', 'Pedro' }
names.add('Carlos')
# removing a element
names.remove('Carlos')
# names.update(['Carlos', 'Ramiro'])

# testing the function with a list
other_list = [ ('Ana', 13), ('Pedro', 24) ]

# validate the test
# if validate_name( 'Carlos', dict(other_list) ) == 0:
    # print( 'El nombre si esta' )
# else:
    # print( 'El nombre no esta' )


if __name__ == '__main__':
    try:
        if validate_name( 'Carlos', dict(other_list)) == 0:
            print( 'El nombre si esta' )

        else:
            print( 'No esta' )

    # en caso la function validate_name lanze el except
    except TypeError as e:
        print( e )
    # from doctest import testmod
    # testmod(verbose=True, name = 'validate_name' )
