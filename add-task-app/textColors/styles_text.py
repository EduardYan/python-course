"""
Aki estan los diferentes estilos para aplicar en main.py y en task.py 
"""
from colorama import Fore, Style, init


# style initials
style_principal_message = Fore.LIGHTBLUE_EX + Style.DIM
style_initial_message = Fore.LIGHTBLUE_EX + Style.BRIGHT

# -----------------------------------
style_task = Fore.LIGHTBLUE_EX + Style.DIM

style_exited = Fore.LIGHTRED_EX + Style.DIM

style_inputs = Fore.LIGHTYELLOW_EX + Style.BRIGHT

style_task_add = Fore.LIGHTCYAN_EX + Style.DIM




# por si ejecutan este archivo
if __name__ == "__main__":
    init(autoreset = True)
    print(Fore.LIGHTRED_EX + Style.DIM + 'Execute main.py')
