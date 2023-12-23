"""
Practica con el modulo subprocess,
es modulo que no permite ejecutar
comandos
"""

from subprocess import call
from colorama import Fore, Style, init
from optparse import OptionParser

# creating a Parser
parser = OptionParser()


# creating the options & argumets at parser
parser.add_option('-k', '--key', dest = 'key', help = "Put the key for execute the Program")
parser.add_option('-f', '--file', dest = 'file', help = "Put the file for open in Vim")

# saving the options or arguments
(options, arguments) = parser.parse_args()


'''
Si queremos ejecutar algun comando podemos usar
la function call(), recibe como parametro el comando para ejecutar
y el parametro shell, si le asignamos True (el interprete anlizara los comandos)
, si le asignamos False (no los analizara), simplemente es para tener un poco
de seguridad
'''
# provando el comando ls para que liste lo que hay en la carpeta
# call( 'ls', shell = True )

# si queremos añadir opciones o argumentos debemos pasarle una lista con el
# comando principal y su argumento u opcion
# call(['ls', '-a'], shell = False)

def validate_key(key):
    """
    Validate the key of file

    """
    # por defecto sera False para cuando
    # entre al statement if retorne el valor en False
    validation = False
    
    # validando la llave
    if not key == 'daniel':
        return validation

    # poniendo la validation a True para retornarla como True,
    # si no entra en el statement if
    validation = True
    # returning the validation
    return validation


# almacenando el valor de la opcion en el parser, en la variable key para evaluarla
key_of_file = options.key
file_to_open = options.file

validation = validate_key(key_of_file)

# validando la validacion
if not validation:
    init(autoreset = True)
    print(
            Fore.LIGHTBLUE_EX + Style.DIM + "Incorrect key for --- {} --- , try again.".format(file_to_open)
            )

else:
    call(f'vim {file_to_open}', shell = True)
