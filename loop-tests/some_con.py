"""
This is a test with not keyword

"""
# name = 'danieliiiiii'


# lim = 10
# if not len(name) > lim:
    # print(f'Name {name} valid')

# else:
    # print(f'Name {name} invalid')


def validate_n(n):
    """
    Return True or False from validation of number
    for paramtrer

    """

    # valiting the number
    if not n > 12:
        return 'The {} not is > to 12.'.format(n)

    return True



n = int(input('Number: '))
