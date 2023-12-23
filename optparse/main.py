"""
This is a test with module optparse
jeje

"""
from optparse import OptionParser
from subprocess import run
import os

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c','--command', dest = 'action' , help = "Escribe el nombre de un comando")

    try:
        (options, args) = parser.parse_args()
        action = options.action
        run(action)

    except TypeError:
        print('main.py required a option or argument. Execute python3 main.py --help')
