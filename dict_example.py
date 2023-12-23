from colorama import init, Fore, Style

# esto es para que los colores de colorama no se hereden y que solo aparescan en las lineas donde llamamos sus propiedades
init(autoreset = True)

def is_good(cost):
    is_good = False

    try:
        if cost <= 2000:
            is_good = True
            return is_good

        # retornando la validacion por defecto sera False
        return is_good

    # por si la funcion recibe un valor que no es numerico
    except TypeError:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + 'the value no is a numeric value')



# a style for show
style_message = Fore.LIGHTBLUE_EX + Style.DIM

try:
    cost_home = int(input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Cost Expeted House: '))

    # creating a casa object
    casa = {
            'cost':cost_home,
            'validation':None

    }

    casa['hola'] = 'Message'

    if 'location' in casa:
        casa.pop('location')
        print('key deleted')

    else:
        print('key not existe')


    print(casa)

    casa['location'] = "San Juan"

    validation = is_good(casa['cost'])

    # validando la validation
    if not validation:
        casa['validation'] = False
        print(style_message + f"Validation: Mala Oferta !!!")

    else:
        casa['validation'] = True
        print(Fore.LIGHTGREEN_EX + Style.DIM + f"Validation: Buena Oferta !!!")


# por si ingresa valores no numericos
# el except lo lanzara la function int
except ValueError:
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 'the value not is a valid value to evaluted')
