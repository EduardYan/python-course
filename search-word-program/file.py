"""
This file have functions for
use in main.py, for work with the
file of user

"""

# for open the file of user
from io import open

def get_file(path_file):
    """
    This function get the file of user
    and return it
    """
    # debemos abrir el archivo en modo lectura(el archivo lo cerraremos en la otra function)
    file = open(path_file, 'r')

    # no hay que cerrar el archivo (lo cerraremos en la funcion get_content_file())
    #file.close()

    # retornando el archivo
    return file


def get_content_file(file):
    """
    This function get the content file
    """
    # leyendo el archivo
    content_file = file.read()

    # cerrando el archivo
    file.close()

    # retornando el contenido archivo
    return content_file


def get_list_words(content):
    """
    This function return the content of file
    but in a list for use in main.py
    """
    # getting the list of words, with .split() function
    list_words = content.split()

    # retornando la lista
    return list_words


def search_word(word, list_word):
    """
    This function searh the word that
    the user say in main.py
    """
    # por defecto la palabra no se encuentra
    search_status = False

    # validando si esta o no esta en la lista de palabras
    if not word in list_word:
        return search_status

    # no es necesario poner el else por que si
    # se cumple la condicion no entrara en su bloque
    # y ejecutara lo siguiente
    search_status = True

    # indice donde se encuentra la palabra del usuario
    index_word = list_word.index(word)
    # palabra en string
    word_found = list_word[index_word]

    # retornando el resultado
    # de la busqueda es False, no entro en
    # el bloque de la condicion no retorna
    # False, si no True y la palabra encontrada
    return search_status, word_found


def show_search(type_exe, word, path_file):
    """
    This function return the result the search
    for show in main.py
    """

    if type_exe == 'True':
        return f'The word {word} is in {path_file}'


    # no es necesario poner else: (por que si la condicion no se cumple no entrara al if)
    return f'The word {word} not in {path_file}'
