from colorama import Fore, Style, init, Cursor
import time
from asyncio import run

async def animation():
    init(autoreset = True)
    print(Fore.LIGHTBLUE_EX + Style.DIM + 'Moving the figure ...')

    while True:
        for progress in ['*-----', '-*----', '--*---', '---*--', '----*-', '-----*']:
            time.sleep(0.5)
            print(Cursor.POS(37, 3) + Fore.LIGHTYELLOW_EX + str(progress))


#print(Cursor.POS(37, 3) + Fore.LIGHTYELLOW_EX + 'ya termino')
move_figure = input('You want to move a figure: ')

async def main():
    if move_figure == 'True':
        await animation()
        print('ksiskw')

    elif move_figure == 'False':
        pass

    else:
        pass

run(main())
