"""
This is a test with module
subprocress
"""

from subprocess import call, PIPE
from io import open

def change_word(word, file):
    """Change a word in the file"""
    if word not in file:
        return "No esta"

    return "Si esta"




output = open('output.txt', 'a')

exe = call( 'ls', stdout = output, stderr = PIPE )

if exe == 0:
    print( 'Good' )
    change_word('app.py', output)

else:
    print( 'Bad' )

# print( output )

