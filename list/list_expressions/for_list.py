"""
Test jeje
"""
names = ['Ana', 'Carlos', 'Valentino', 'Pablo']

for n in range(len(names) - len(names)):
    try:
        print(names[n])

    except IndexError:
        pass

