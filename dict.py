"""
This is a test with a dict function

"""
from app import change_caracter

# ------ FUNCTIONS -------
# Return a object for use in the execution
get_object = lambda list_v : dict(list_v)
# This function return a list for use
get_list = lambda tuple_1, tuple_2 : [ tuple_1, tuple_2 ]
# Add the user at list of users
add_user = lambda user, list_users : list_users.append( user )

def show_users(list_users):
    """
    This function show the user in
    the list

    """
    for u in list_users:
        format_show = 'Name: ' + u['nameUser'] + ' Age: ' + str(u['ageUser'])
        print(format_show)


# aki se guardaran los usuarios
list_u = []

# getting data of user
name = input('Name > ')
# name = change_caracter(len(name) - 1, '%', name)
name.replace('%', len(name) - 1)
age = input('Age > ')

# ---- Processing Users ----
# getting the list with tuples for converter in a object
list_c = get_list( ('nameUser', name), ('ageUser', age) )
# getting the user with the get_object function
user = get_object(list_c)


if __name__ == '__main__':
    # agregando el usuario
    add_user(user, list_u)
    # showing the users
    show_users(list_u)
