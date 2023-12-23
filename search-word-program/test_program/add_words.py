"""
This file add words, in a file
for debug the main.py program

"""

from io import open

def get_file(name_file):
    """
    Return a file for add word
    """
    file = open(name_file, 'a')

    return file

# list with words
list_words = (
        'archivo',
        'para',
        'debujear',
        'el',
        'programa',
        'de',
        'buscar',
        'palabras',
        'en',
        'un',
        'texto'
        )

def add_words(file):
    """
    This function add the words at
    file
    """
    for word in list_words:
        formato = word + '\n'
        file.write(formato)

    return 'Words Added'

# ---- Logic for add words ------
FILE = 'list_words.txt'
my_file = get_file(FILE)
print( add_words(my_file) )
