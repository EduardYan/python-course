"""
This is a test with function globals
"""

a = 56

def someting():
    globals()['a'] = 12
    print(a)

someting()
print(a)
