"""
This is a test program practice

"""
# for use colors
# from colorama import Fore, Style, init
# from is_empty import is_empty_list

is_empty_list = lambda lista: isinstance(lista, list)


def join_word(word, list_words):
    # using the global var words
    global words

    # agregando la palabra ala lista de palabras
    list_words.append(word)

    # cada vez que se agrega aumentamos ala variable
    words += 1

    return list_words


def show_history(list_words):
    """
    This function show the words added in the list_words
    """
    # showing each word in the list
    for word in list_words:
        print(Fore.BLUE + Style.BRIGHT + f'''                            {word}''')

    print(Style.RESET_ALL)


# aki se guardaran todas las palabras
list_words = []
# adding more elements
list_words.extend( [133, 444, 55] )

# limpiando la lista solo para practicar con las listas
# list_words.clear()

# for count the words
words = 0

if __name__ == '__main__':
    while True:
        # para que el color se resete el solo
        init(autoreset=True)

        word = input(Fore.MAGENTA + 'Word: ')

        ''' validando para poder salir del bucle o ejecutar las funciones '''
        if word == 'e':
            # saliendo del bucle
            break

        # por si se ingresa algun numero
        elif word.isdigit():
            print(Fore.CYAN + Style.DIM + '\nEnter Numeric Values')

        else:
            ''' executing alls functions '''
            join_word(word, list_words)

            # showing the last addede word
            print(Fore.GREEN + Style.DIM + 'Palabras añadidas: ', words)

            # showing the added words
            show_history(list_words)

            # validando si la lista esta vacia
            if is_empty_list(list_words):
                print('esta vacia')
            else:
                print('no esta vacia')

    # para cuando salga del bucle
    print(Fore.RED + Style.BRIGHT + 'Exited the Program')
