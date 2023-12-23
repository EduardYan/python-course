"""
Join strings of a list
"""

from app import Message

def get_string(list_str):
    """
    Return a string
    """
    new_string = ''

    for s in list_str:
        new_string += s

    return new_string

o = get_string([n for n in 'hola'])
print(o)
print(type(o))

name = 'abde'
message = Message(name)
message_encrypted = message.encrypt()
message_de = message.decrypt(message_encrypted)

print(message_de)
