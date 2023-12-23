"""
This is a program for verify
if a name is correct.
"""



def is_caracter(name, caracteres):
    """
    Verify if a caracter is a name
    """
    if type(name) not in [str]:
        raise TypeError('The parameter {name} must be a string.')

    if type(caracteres) not in [list, tuple]:
        raise TypeError('The parameter {caracteres} must be a list or tuple.')

    for c in caracteres:
        if c in name:
            return True

    return False


def is_valid_name(name):
    """
    Verify a name.
    """
    # for if the name not is a string
    if type(name) not in [str]:
        raise TypeError('The parameter {name} must be a string.')

    # verify the name
    is_valid = is_caracter(name, [']', '/', '-', '=', ',', ';'])
    if is_valid:
        return False

    return True


if __name__ == '__main__':
    name = input('Name for verify: ')
    try:
        # verify the name of the user
        if is_valid_name(name):
            print(Fore.GREEN + f'The name {name} is valid.')

        else:
            print(Fore.RED + f'The name {name} not is valid.')

    except TypeError as e:
        print(e)
