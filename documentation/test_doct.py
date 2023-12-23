"""
This is a example with python documentation test

"""

def add(n1 : int , n2 : int):
    """
    Return the add of two values

    """
    return n1 + n2

def get_list_names(names : list):
    """
    Return a list of names from names parametrer

    """

    if not isinstance( names, list ):
        raise TypeError( "Error. Not are lists." )
        return "Error. Not are lists"

    list_names = []
    for n in names:
        list_names.append( n )


    return tuple(list_names)

if __name__ == '__main__':
    # hay dos formas para hacer la prueba
    # ----- first form -----
     from doctest import testmod
    # le podemos dar el nombre de la funcion en la cual queremos
    # que haga el test
    testmod(name = 'get_list_names')

    # ----- second form -----
    # import doctest
    # doctest.testmod()
