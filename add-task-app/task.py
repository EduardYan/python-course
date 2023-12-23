"""
Este archivo tiene la clase para crear la tarea y sus distintos metodos para 
utilizar en main.py
"""

# Estilos de colorama
from textColors.styles_text import style_exited, style_inputs, style_task_add, style_task
# documento para guardar las tareas
from file import get_file, get_format_task
from colorama import init
from datetime import date

# this variable is for aumentar el contador del numero de la tarea
C = 1
C_2 = 1
# creating the date for save in self.__task hay que convertirlo a string sino obtenemos el objecto
date = str(date.today())


class Task():
    def __init__(self, titleTask, descriptionTask, date_finally):
        # creando el objeto de la tarea eatara encapsulado para que no lo utilizen fuera de esta clase
        self.__task = {
                'numberTask':C,
                'title':titleTask,
                'description': descriptionTask,
                'date_created': date,
                'date_finally': date_finally
        }

    def save_task(self, list_task):
        """ this function added the self.__task at list_task """

        # using the global c
        global C

        """ Working the list in memory """
        # save the list in a property
        self.list_task = list_task
        # added the self.__task at list
        self.list_task.append(self.__task)
        # aumentando el numero de la tarea
        C += 1

        """ Working with the file """
        format_task = get_format_task(self.__task)
        file_created = get_file('list_tasks.txt')

        # por si utilizan la funcion y no la clase
        #file_created = give_file('list_tasks.txt')

        # write the object task in the file
        file_created.write(format_task)
        file_created.close()


    def show_task_add(self):
        """ this method show the task added with a for """

        global C_2

        print(style_task_add + f"Task Added ------- {C_2} ------ {self.__task['title']} _____ {self.__task['description']}")

        C_2 += 1

        # showing tasks of the list in memory not is the file where save the task
        for task in self.list_task:
            print(style_task + f"Title: {task['title']}  Description: {task['description']} Date to Finish: {task['date_finally']}")


# por si ejecutan este archivo
if __name__ == "__main__":
    init(autoreset = True)
    print(style_exited + 'Execute main.py')
