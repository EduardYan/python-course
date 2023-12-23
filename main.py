"""
Program for found name
"""

def found_name(name, list_names):
    """ Return the result of validation """
    if not name in list_names:
        return 'No hemos encontrado el nombre en la lista'

    # encontrando the index
    index = list_names.index(name)
    # returning
    return f'Hemos encontrado el valor en el indice {index}.'


# list for do the test
list_names = ['Ana', 'Pedro', 'Juan']

if __name__ == '__main__':
    name_to_find = input('Name To Find > ')

    search_result = found_name(name_to_find, list_names)
    print( search_result )

    # showing the list with your content
    print('List' + '\n' + str(list_names))
