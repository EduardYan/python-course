"""
This is the principal file.
Add Product Program.

"""
# for create the parser
from optparse import OptionParser
# for remove the file
from subprocess import call
# for create the sale
from sale import Sale
# for get list_products
from list_products import get_list_products


# --------- Creating the Parser --------
parser = OptionParser()

# add a new option
parser.add_option('-r', '--rf', dest = 'type_exe', help = "Remove the file where to go, save the products of sales.")

# saving the options or arguments
(options, arguments) = parser.parse_args()


# initial messages for show
initial_message = """
    [ Add a Product with a Name & Price ]
"""

# for show the total sales
total_sales = 0

# getting the list_products
list_products = get_list_products()


def main(type_exe):
    """
    This is a principal function

    """
    # for get it value, for adding it value
    global total_sales

    # showing the initial_message
    print( initial_message )

    # Loop Program
    while True:
        name = input('\nName Product: ')

        if name.isdigit():
            print( "Not Enter Numeric Values." )

        # for exit the while loop
        elif name == 'e':
            # saliendo del while loop
            break

        else:
            try:
                price = int( input('Price Product: ') )

                # ----- Working with Sale ------
                sale = Sale(name, price)
                # adding the sale
                sale.add_sale('products_saved.txt', list_products)
                # aumentando la cantidad ventas
                total_sales += 1

                # printing total of sales
                print(f'[+] New Sale ------- Total Sales {total_sales}')

                # showing the sales
                sale.show_products(list_products)

            except ValueError:
                print('Enter Numeriv Values')

    # validando el tipo de ejecucion
    # cuando salga de while loop, para decidir si eliminar el
    # archivo
    if type_exe == 'yes':
        # remove the file
        call( ['rm', 'products_saved.txt'], shell = False )
        print('Exited:)}')

    elif type_exe == 'no':
        # for exit the while loop, without remove file
        # where is the sales
        print('Exited:)')

    else:
        print('Elige un tipo de ejecucion. Please')



if __name__ == '__main__':
    # getting the option of parser
    type_exe = options.type_exe

    # pasandole a la function the type of execution
    main( type_exe )
