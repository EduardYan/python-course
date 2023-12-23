from colorama import Fore, Style, init

style_one = Fore.LIGHTGREEN_EX + Style.DIM
style_two = Fore.CYAN + Style.DIM
style_three = Fore.LIGHTMAGENTA_EX + Style.DIM
style_four = Fore.BLUE + Style.DIM

styles_list = [style_one, style_two, style_three, style_four]

init(autoreset = True)

# ver las diferencias entre los dos bucles
# este cambia el estilo de forma vetical porque la variable de
# la longuitud del color no cambia cada vez que se ejecuta el principal for
# loop.
for i in range(len(styles_list)):
    for j in range(4):
        print(styles_list[j] + '/ ', end = '')
    print()

print('----- -------')

# este de forma horizontal
for i in range(len(styles_list)):
    for j in range(4):
        print(styles_list[i] + '/ ', end='')

    print()
