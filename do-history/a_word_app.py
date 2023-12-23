"""
This is a principal file.
This Program can create a history and show it

"""

# for show colors
from colorama import Fore, Style, init

# this function add the word at list
join_word = lambda list_word, word_add : list_word.append(word_add)

def show_history(list_word):
    """ Show the values in the list_word """

    # style of history
    STYLE_HISTORY = Fore.LIGHTCYAN_EX + Style.BRIGHT

    # recorriendo the list for show each word in the list of words
    for w in list_word:
        format_h = STYLE_HISTORY + f"           {w}"
        print( format_h )


# here save the words
list_word = []

if __name__ == '__main__':
    init( autoreset = True )
    while True:
        word = input('Word: ')

        # for exit
        if word == 'e':
            break

        # if the word is a number
        elif word.isdigit():
            print( Style.BRIGHT + 'Enter a Word Please.' )

        else:
            # join the words
            join_word( list_word, word )
            # showing the history
            show_history( list_word )

    # for when exit the while loop
    print( Fore.LIGHTRED_EX + Style.BRIGHT + 'Exited :}' )
