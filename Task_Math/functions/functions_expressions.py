"""
This are functions in expressions
"""


def say_hello(name):
    """Return a message with the name"""
    return 'Hola ' + name


messages = [say_hello(n) for n in ['Ana', 'Juan', 'Ramiro']]

for m in messages:
    print(m)
