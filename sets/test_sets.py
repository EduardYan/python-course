"""
Test with sets
"""

names = {'Ana', 'Carlos', 'Ramiro'}

names_2 = {'Ana', 'Carlos'}

if names_2.issubset(names):
    if 'Ana' in names_2:
        names_2.remove("Ana")

    print('yes')

else:
    print('no')

print(names_2)
