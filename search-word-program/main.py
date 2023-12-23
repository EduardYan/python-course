"""
This is principal file

Search a word in a file

"""

# ------ IMPORTS -------
# only use the init function
from colorama import init
# for make the logic with the file of user
from file import get_file, get_content_file, search_word, get_list_words, show_search
# for show mesaages in case error
from messages.show_messages import IS_NUMERIC_ERROR, HELP_INPUT_FILE, HELP_INPUT_WORD
# for show mesaages in case error
from messages.show_messages import INITIAL_MESSAGE, IS_A_DIRECTORY_ERROR, FILE_NOT_FOUND
# for add styles of messages
from colors.text_styles import STYLE_EXIT, STYLE_ERROR_FILE, STYLE_IS_NUMERIC
from colors.text_styles import STYLE_MESSAGES_INITIALS, STYLE_OF_CONTENT
from colors.text_styles import STYLE_INPUT_FILE, STYLE_INPUT_WORD


def main():
    """
    This a principal function

    """
    # para que los colores de colorama no se hereden
    init(autoreset = True)

    # showing the initial_message in show_messages.py
    print( STYLE_MESSAGES_INITIALS + INITIAL_MESSAGE )
    print( STYLE_MESSAGES_INITIALS + HELP_INPUT_FILE )
    print( STYLE_MESSAGES_INITIALS + HELP_INPUT_WORD )


    # ------- Principal Loop for repeat the code -----
    while True:
        # getting the path of file
        path_file = input( STYLE_INPUT_FILE + 'Path Of File > ' )


        # por si lo que ingresa son numeros y no la direccion
        if path_file.isdigit():
            # showing the message
            print( STYLE_IS_NUMERIC + IS_NUMERIC_ERROR )

        # for exit the while loop
        elif path_file == 'e':
            # exiting the while loop
            break


        else:
            word_to_find = input(STYLE_INPUT_WORD + 'Word To Find > ')

            # Controlando los excepts de abrir el archivo del usuario
            try:
                # getting the file of user
                file_of_user = get_file( path_file )

                # getting the content_file
                content_file = get_content_file( file_of_user)

                # getting list of words of content_file
                list_words = get_list_words( content_file )

                try:
                    # searching the word & almacenando la palabra encontrada
                    # si no la funcion no retorna la palabra, significa que la
                    # palabra no esta ver funcion search_word en file.py
                    search_status, word_found = search_word( word_to_find, list_words )

                    # if search_status == True
                    if search_status:
                        # mostrando el contenido del archivo
                        print( STYLE_OF_CONTENT + '\n' + content_file )
                        print('Word: ' + word_found)

                        print( show_search('True', word_to_find, path_file) )


                # capturando el execpt si la funcion search_word solo
                # retorna el estado y no el estado y la palabra que el usuario
                # queria buscar, porque la intentamos almacenar en bloque try en la
                # ejecucion de la funcion
                except TypeError:
                    print( STYLE_OF_CONTENT + '\n' + content_file )
                    print( show_search('False', word_to_find, path_file) )


            # Los excepts vienen de la ejecucion
            # de la funcion io.open() en file.py
            # por si no encuentra el file
            except FileNotFoundError:
                print( STYLE_ERROR_FILE + FILE_NOT_FOUND )

            # por si es un directorio
            except IsADirectoryError:
                print( STYLE_ERROR_FILE + IS_A_DIRECTORY_ERROR )


    # for exit the while loop
    print( STYLE_EXIT + "Exited:}) Bye" )

if __name__ == '__main__':
    # executing the principal function
    main()
