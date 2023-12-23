"""
Union with sets
"""

teachers = {'Ana', 'Mary', 'Carlos'}

# union method recive a sets
# for add in the set object
# es buena idea guardarlo en una variable
new_set = teachers.union( {'Ana', 'Juan'} )

# see diferences
print(new_set)
print(teachers)

# teachers = { 'Ana', 'Pedro', 'Carlos' }

# c = {'Ana', 'Pedro'}
# intersection return a set with the concidencias
# # print(teachers.intersection( c ))
