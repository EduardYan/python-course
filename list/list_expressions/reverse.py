"""
We can do this in the lists
"""

names = ['Natalia', 'Pedro', 'Varmen']
last = names[-1]
print(last)

numbers = [23, 45, 90.2, 3.4]
print(numbers)
del numbers[-2]
print(numbers)


children = ['Carlos', 'Oscar', 'Fabian']
last = children[len(children) - 1]
if last == 'Fabian':
    del children[len(children) - 1]

print(children)
