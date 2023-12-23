"""
Este archivo tiene la clase File que retorna un archivo en el cual se guardaran
de forma permamente las tareas del usuario
"""

from textColors.styles_text import style_exited
from colorama import init

"""
Tenemos dos opciones para crear el archivo por medio del
metodo de una clase o simplemente una funcion
(no si usar funcion o clase)
si usan la funcion tendran que modificar task.py
"""


def get_file(nameFile):
    """ this function retur a file for use in task.py"""
    file = open(nameFile, 'a')

    # no hay que cerrar el archivo aki, en task.py si lo cerramos hay que retornarlo abierto
    # file.close()

    return file


def get_format_task(task):
    """
    This function return the format of task
    for save in task.py in the file
    """
    # saving for use
    title = task['title']
    description = task['description']
    date_created = task['date_created']
    date_finally = task['date_finally']

    # doing the format
    format_task = title + ' ----- ' + description + ' ----- ' + 'Date Created: ' + date_created + ' ----- ' + 'Date to Finally: ' + date_finally + '\n'

    # returning the format of task
    return format_task


# por si ejecutan este archivo
if __name__ == "__main__":
    # using init from colorama
    init(autoreset=True)
    print(style_exited + 'Execute main.py')
