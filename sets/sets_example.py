"""
Practice with set
"""

class Name:
    """ Create a Name """
    def __init__(self, content):
        # creating longuitud y contenido
        self.lon = len( content )
        self.content = content

    def get_name(self):
        """
        Return the name
        """
        name = str(self.content)
        lon = self.lon
        return name, lon


def do_names(list_names):
    """
    Do names from class
    """
    c = 0
    while c < len(list_names):
        n = Name( list_names[c] )
        name, lon = n.get_name()

        print( f"Name {name} > Letters {lon}" )

        c += 1

# list of names
list_names = ['Carlos', 'Ana', 'Juan']
# add elements
list_names.extend( ['Nario', 'Marleni', 'Table'] )

if __name__ == '__main__':
    # doing the names
    do_names( list_names )
