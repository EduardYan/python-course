"""
This file is for create the sale
Have class Sale for use in main.py.

Also have a function for add the sale
at list_products.

"""

# for work with file
from io import open

class Sale():
    """
    Create a Sale

    """
    def __init__(self, name_product, price_product):
        # creating the object, this property is encapsulated
        self.__sale = {
                'name': name_product,
                'price': price_product

                }

    def add_sale(self, path_file, list_products):
        """
        Add the sale at
        list of products

        """
        # for add a new line, for each sale
        format_s = 'Name ----- ' + self.__sale['name'] + ' Price ------- ' + str(self.__sale['price']) + ' \n'
        # adding the sale at a file
        file = open(path_file, 'a')
        # write in the file
        file.write(format_s)

        # adding the sale
        list_products.append(self.__sale)


    def show_products(self, list_products):
        """
        Show the products in the list of
        products

        """

        print("Products ----------------- ")
        # showing
        for p in list_products:
            format_p = f"           {p['name']} {p['price']}"
            print(format_p)
