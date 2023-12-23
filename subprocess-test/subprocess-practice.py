"""
This is a test with the module
subprocess

"""

# from os import open, devnull
from io import open
from subprocess import call, STDOUT

file = open('output.txt', 'w')

process = call( ['curl', 'www.google.com'], stdout = file, stderr = STDOUT )

if process == 0:
    print( 'todo salio bien' )

else:
    print( 'algo salio mal' )
