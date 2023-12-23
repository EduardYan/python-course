"""
Este es el archivo principal
"""

# for create the Task
from task import Task
# for init(autoreset = True)
from colorama import init
# for execute commands in Linux and remove the file where it's the users's task
import subprocess
# Estilos de colorama
from textColors.styles_text import style_exited, style_inputs, style_task_add, style_task, style_initial_message, style_principal_message
# for get list
from listTask import give_list
# for show messages
from messages.errors import numeric_error
# for show messages in the function main()
from messages.show_messages_initials import initial_message, principal_message
# for to do the parser
from optparse import OptionParser

""" Parser
for execute the program removing the file:
python3 main.py -r y [yes]
python3 main.py --rf y [yes]


for execute the program & not removing the file:
python3 main.py -r n [no]
python3 main.py --rf n [no]
"""
parser = OptionParser()
# como destino tendra la variable remove_file para luego validar sobre la ejecucion de la funcion principal main()
parser.add_option('-r', '--rf', dest = 'remove_file', help = 'Decide si eliminar el archivo donde se guardaran tus tareas') # Go


# pasando los argumentos y opciones
(options, arguments) = parser.parse_args()


# aki se guardaran las tareas en memoria la lista la obtenemos de la funcion en el modulo listTask.py
list_task = give_list()

def main(type = 'yes'):
    """ Esta es la funcion principal
    que ejecuta todo por default el tipo
    de ejecucion sera 'yes'
    """

    ''' Por si la lista que obtenemos contiene elementos
    tambien podemos validar asi:
    if list_task != []:
    pero yo prefiero esta forma
    '''
    if len(list_task) != 0:
        raise TypeError('La lista ya contiene otros elementos')

    else:
        # para que los colores de colorama no se hereden y solo se ejecuten en las lineas que le decimos
        init(autoreset = True)

        # this we'll show when execute program

        # show initial_message
        print(style_initial_message + initial_message)

        """ PRINCIPAL LOOP """
        while True:
            titleTask = input(style_inputs + 'Title Task: ')


            # para que el usuario salga
            if titleTask == 'e':
                # saliendo del while loop
                break


            # por si lo que ingresa son numeros
            elif titleTask.isdigit():
                print(numeric_error)

            else:
                descriptionTask = input(style_inputs + 'Description Task: ')

                # por si en la description de la tarea ingresa numeros
                if descriptionTask.isdigit():
                    print(numeric_error)

                # exit in descriptionTask
                elif descriptionTask == 'e':
                    # exiting
                    break

                else:
                    # saving the finish task
                    date_finally = input('Date to Finish the task: ')

                    """ Working the Task of the user """
                    task = Task(titleTask, descriptionTask, date_finally)
                    task.save_task(list_task)
                    task.show_task_add()

        # para cuando salga del while loop
        print(style_exited + '\nExited:})')


        # ---------------------------------
        """ Si el tipo de ejecucion de esta funcion es 'yes' pues eliminaremos el
        archivo donde guardamos las tareas del usuario
        """
        if type == 'yes':
            """ Aki con el modulo subprocess ejecutamos el comando para que elimine el list_task.txt
            donde se guardan las tareas del usuario
            si el archivo no existe no nos tirara una exepcion si el mensage de el bash de Linux'
            """
            ''' Eliminando el file where is use's task
            solo utilizo esto en dev para que borre el archivo por mi
            '''
            subprocess.call('rm list_tasks.txt', shell = True)

        else:
            # para que no haga nada y vuelva bucle principal
            pass

        # ---------------------------------

if __name__ == '__main__':
    init(autoreset = True)

    # showing principal_message
    print(style_principal_message + principal_message)


    ''' Almacenando los valores de las opciones o argumentos
    remove_file para luego validar
    '''
    remove_file = options.remove_file


    """ Disidiendo el tipo de ejecucion of the function main() """
    if remove_file == 'yes' or remove_file == 'y':
        main('yes')

    elif remove_file == 'no' or remove_file == 'n':
        main('no')

    # por si el usuario presiona <Enter> el valor por defecto de main() sera 'yes'
    elif remove_file == '':
        main()

    else:
        print('Please enter a execute option')
